<center><img src="https://live.staticflickr.com/4234/35829948885_7f49bca92a_h.jpg" alt="Valve Image from Flickr" width="500"/></center>
<!-- https://www.flickr.com/photos/cogdog/35829948885/ -->

# Valve


A collection of tools for handling data lake administration.  It's primarily a UI to [databasin][0], developed by [TPI][1].

It's currently both a CLI and python wrapper to the databasin [REST API][2].

# Installation

    pip install git+https://github.com/i2-wustl/valve.git@main

# Usage

## CLI Interface

```
$ valve --help
Usage: valve [OPTIONS] COMMAND [ARGS]...

  A collection of related tools for handling data lake administration.

Options:
  --version   Show the version and exit.
  -h, --help  Show this message and exit.

Commands:
  howdy  subcommand template
```

Addtionally, try `valve <subcommand> --help` for more details on a particular subcommand.

## python interface

```python
import valve.core.api as api
debug = True
api.hello(debug)
```

## Documentation

For further information please see the corresponding [documentation site][3] _(Coming soon!)_

# Development

## Environment Setup

### Step 1:  Clone and enter the repository

    git clone git@github.com:i2-wustl/valve.git valve
    cd valve

### Step 2: Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install the code as a "editable" installation

```bash
pip install -e .
```

### Step 4: Develop away!

## Testing

[0]: https://demo.databasin.co
[1]: https://technologypartners.net
[2]: https://demo.databasin.co/api/docs/swagger-ui/index.html?url=https://demo.databasin.co/api/swagger.json#/
[3]: https://www.google.com
