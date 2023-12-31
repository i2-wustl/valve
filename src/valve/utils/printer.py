import json
import sys
import tabulate as t

valid_formats = [ 'json', 'cjson', 'tsv', 'table', 'ctable', 'html' ]

class Printer():
    def __init__(self, data=None):
        self.raw_data = data
        self.max_list_value_column_width = 100

    def render(self, format='json', columns='all'):
        if format not in valid_formats:
            msg = f"[err] Not a valid printer format: {format}"
            raise Exception(msg)

        method_name = self._derive_render_method(format)
        columns = self._derive_data_columns(columns)
        method = getattr(self, method_name)
        return method(columns=columns)

    def _derive_render_method(self, format='json'):
        method = '_'.join(['_render', format])
        return method

    def _derive_data_columns(self, columns):
        if columns == 'all':
            return self._get_all_columns()
        return columns

    def _get_all_columns(self):
        columns = None
        if isinstance(self.raw_data, list) and self.raw_data:
            columns = sorted(self.raw_data[0].keys())
        elif self.raw_data:
            columns = sorted(self.raw_data.keys())
        return columns

    def _filter_data(self, columns):
        if isinstance(self.raw_data, list) and self.raw_data:
            # assuming each element in list is a dictionary containing row data
            filtered_data = []
            for d in self.raw_data:
                filtered = { c: d[c] for c in columns }
                filtered_data.append(filtered)
            return filtered_data
        elif isinstance(self.raw_data, dict):
            # assuming simple dictionary -- construct attribute/value table
            filtered = { c: self.raw_data[c] for c in columns }
            return filtered
        else:
            msg = "[err] Printer does not know how to filter the data"
            raise Exception(msg)

    def _construct_tabulate_data_table(self, data, columns):
        if isinstance(data, list):
            # assuming each element in list is a dictionary containing row data
            table = { c: [] for c in columns }
            for row in data:
                for c in columns:
                    value = self._format_entry(row[c])
                    table[c].append(value)
            return table
        elif self._is_data_in_tabulate_format(data):
            return data
        else:
            # assuming simple dictionary -- construct attribute/value table
            table = [[c, self._format_entry(data[c])] for c in columns]
            return table

    def _is_data_in_tabulate_format(self, data):
        # tablulate format is a dictionary of the form:
        # {
        #    'column_name_1' : [a_value1, a_value2, c_value3],
        #    'column_name_2' : [b_value1, b_value2, c_value3],
        #    ...
        # }
        # Note: all the list values have the same size
        if not isinstance(data, dict):
            return False

        # ensure all column key values are lists
        for column in data.keys():
            if not isinstance(data[column], list):
                return False

        # ensure all column key values have the same size
        column_lengths = set([len(data[c]) for c in data.keys()])
        if len(column_lengths) != 1:
            return False

        return True

    def _format_entry(self, datum):
        if isinstance(datum, list):
            return self._collapse_list(datum)
        elif isinstance(datum, int):
            return str(datum)
        else:
            return datum

    def _collapse_list(self, listdata):
        full_string = ' | '.join(listdata)
        max_column_width = self.max_list_value_column_width
        if len(full_string) > max_column_width:
            return full_string[:max_column_width]
        return full_string

    def _render_json(self, columns):
        filtered = self._filter_data(columns)
        print(json.dumps(filtered, sort_keys=True, indent=2))

    def _render_cjson(self, columns):
        filtered = self._filter_data(columns)
        import rich.console
        console = rich.console.Console()
        console.print_json(json.dumps(filtered, sort_keys=True))

    def _render_tsv(self, columns):
        filtered = self._filter_data(columns)
        table = self._construct_tabulate_data_table(filtered, columns)
        if isinstance(filtered, list) or self._is_data_in_tabulate_format(table):
            print(t.tabulate(table, headers="keys", tablefmt='tsv'))
        elif isinstance(filtered, dict):
            print(t.tabulate(table, headers=['attribute', 'value'], tablefmt='tsv'))
        sys.stdout.flush()

    def _render_table(self, columns):
        filtered = self._filter_data(columns)
        table = self._construct_tabulate_data_table(filtered, columns)
        if isinstance(filtered, list) or self._is_data_in_tabulate_format(table):
            print(t.tabulate(table, headers="keys", tablefmt='simple'))
        elif isinstance(filtered, dict):
            print(t.tabulate(table, headers=['attribute', 'value'], tablefmt='simple'))
        sys.stdout.flush()

    def _render_html(self, columns):
        filtered = self._filter_data(columns)
        table = self._construct_tabulate_data_table(filtered, columns)
        data = '[err] printing trouble'
        if isinstance(filtered, list) or self._is_data_in_tabulate_format(table):
            data = t.tabulate(table, headers="keys", tablefmt='html')
        elif isinstance(filtered, dict):
            data = t.tabulate(table, headers=['attribute', 'value'], tablefmt='html')
        return data

    def _render_ctable(self, columns):
        raise Exception("Please implement me!")
