#!/usr/bin/env python3

import sys
import json
import tabulate


def main():
    if sys.stdin.isatty():
            print('missing piped data')
            sys.exit(1)

    pipe_data = sys.stdin.read()

    try:
        data = json.loads(pipe_data)
        if type(data) is not list:
            data_list = []
            data_list.append(data)
            data = data_list

    except Exception:
        # if json.loads fails, assume the data is formatted as json lines and parse
        data = pipe_data.splitlines()
        data_list = []
        for jsonline in data:
            entry = json.loads(jsonline)
            data_list.append(entry)

        data = data_list

    # wrap every 17 chars for all field values
    for entry in data:
        for k, v in entry.items():
            if v is not None:
                entry[k] = '\n'.join([str(v)[i:i + 17] for i in range(0, len(str(v)), 17)])

    print(tabulate.tabulate(data, headers='keys'))


if __name__ == '__main__':
    main()