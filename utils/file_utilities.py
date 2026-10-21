import csv
from typing import Optional, Union, overload
import openpyxl


class FileUtility:

    @overload
    @staticmethod
    def read_csv_file(file_path: str) -> list[dict[str, str]]:
        """Read an entire CSV file into a list of row dictionaries.

        Parameters
        ----------
        file_path : str
            The path to the CSV file to read.

        Returns
        -------
        list[dict[str, str]]
            A list where each item represents a row mapped by column headers.

        Usage
        -----
        >>> rows = FileUtility.read_csv_file("data/users.csv")
        """
        ...

    @overload
    @staticmethod
    def read_csv_file(file_path: str, header: str, row: int) -> str:
        """Read a specific cell value from a CSV file.

        Parameters
        ----------
        file_path : str
            The path to the CSV file to read.
        header : str
            The column header name to retrieve.
        row : int
            The 0-based row index.

        Returns
        -------
        str
            The cell value at the specified row and column.

        Usage
        -----
        >>> email = FileUtility.read_csv_file("data/users.csv", "email", 0)
        """
        ...

    @staticmethod
    def read_csv_file(
        file_path: str,
        header: Optional[str] = None,
        row: Optional[int] = None,
    ) -> Union[list[dict[str, str]], str]:
        """Read all rows or a single cell from a CSV file.

        Parameters
        ----------
        file_path : str
            The path to the CSV file to read.
        header : str, optional
            Column name. If supplied with `row`, returns that single cell value.
        row : int, optional
            0-based row index. Required if `header` is provided.

        Returns
        -------
        list[dict[str, str]] or str
            List of row dicts if header/row are omitted; single cell string otherwise.

        Raises
        ------
        ValueError
            If only one of `header` or `row` is provided.
        IndexError
            If `row` index is out of bounds.
        KeyError
            If `header` does not exist in the CSV columns.

        Author: Saurabh Kushwaha
        Date: 2026-10-08
        """
        with open(file_path, mode="r", encoding="utf-8") as file:
            records = list(csv.DictReader(file))

        # Handle single cell extraction
        if header is not None and row is not None:
            return records[row][header]

        # Handle entire file extraction
        if header is None and row is None:
            return records

        raise ValueError("Both 'header' and 'row' must be provided together.")

    @staticmethod
    def read_excel_file(file_path: str, sheet: str, row: int, column: int):
        wb = openpyxl.load_workbook(file_path, data_only=True)
        try:
            ws = wb[sheet]
            return ws.cell(row=row + 1, column=column + 1).value
        finally:
            wb.close()
