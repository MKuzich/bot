"""Table output"""
from tabulate import tabulate

def table_output(data_for_table, headers, tablefmt, missingval,  maxcolwidths, caption=""):
    """Generate a table. !missingval do not working with maxcolwidths if one of elem.tbl is None"""

    return "\n" + caption + tabulate(data_for_table, headers,
                                     tablefmt=tablefmt,
                                     missingval=missingval,
                                     maxcolwidths=maxcolwidths) + "\n"
