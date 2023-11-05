import json
import sys
import tabulate as t

valid_formats = [ 'json', 'cjson', 'tsv', 'table', 'ctable' ]

class Printer():
    def __init__(self, data=None):
        self.data = data

    def render(self, format='json', columns='all'):
        if format not in valid_formats:
            msg = f"[err] Not a valid printer format: {format}"
            raise Exception(msg)

        method_name = self._derive_render_method(format)
        columns = self._derive_data_columns(columns)
        method = getattr(self, method_name)
        method(columns=columns)

    def _derive_render_method(self, format='json'):
        method = '_'.join(['_render', format])
        return method

    def _derive_data_columns(self, columns):
        if columns == 'all':
            return self._get_all_columns()
        return columns

    def _get_all_columns(self):
        columns = None
        if isinstance(self.data, list) and self.data:
            columns = sorted(self.data[0].keys())
        elif self.data:
            columns = sorted(self.data.keys())
        return columns

    def _filter_data(self, columns):
        if isinstance(self.data, list) and self.data:
            filtered_data = []
            for d in self.data:
                filtered = { c: d[c] for c in columns }
                filtered_data.append(filtered)
            return filtered_data
        elif isinstance(self.data, dict):
            filtered = { c: d[c] for c in columns }
            return filtered
        else:
            msg = "[err] Printer does not know how to filter the data"
            raise Exception(msg)

    def _construct_tabulate_data_table(self, data, columns):
        if isinstance(self.data, list):
            table = { c: [] for c in columns }
            for row in data:
                for c in columns:
                    table[c].append(row[c])
            return table
        else:
            table = [[c, data[c]] for c in columns]
            return table

    def _render_json(self, columns):
        filtered = self._filter_data(columns)
        print(json.dumps(filtered, sort_keys=True, indent=4))

    def _render_cjson(self, columns):
        filtered = self._filter_data(columns)
        import rich.console
        console = rich.console.Console()
        console.print_json(json.dumps(filtered, sort_keys=True))

    def _render_tsv(self, columns):
        filtered = self._filter_data(columns)
        table = self._construct_tabulate_data_table(filtered, columns)
        if isinstance(filtered, list):
            print(t.tabulate(table, headers="keys", tablefmt='tsv'))
        elif isinstance(filtered, dict):
            print(t.tabulate, table, headers=['attribute', 'value'], tablefmt='tsv')
        sys.stdout.flush()

    def _render_table(self, columns):
        filtered = self._filter_data(columns)
        table = self._construct_tabulate_data_table(filtered, columns)
        if isinstance(filtered, list):
            print(t.tabulate(table, headers="keys", tablefmt='simple'))
        elif isinstance(filtered, dict):
            print(t.tabulate, table, headers=['attribute', 'value'], tablefmt='simple')
        sys.stdout.flush()

    def _render_ctable(self, columns):
        raise Exception("Please implement me!")

