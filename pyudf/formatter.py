from numbers import Number


class Formatter:
    """This class has format functions to make params valid for gourmet.
    """

    def _format_value(self, contents):
        """Format dict and str for gourmet.

        Parameters
        ----------
        contents: dict
            Keys are valid for udf file and values are dict or str.

        Note
        ----
        This is a bang method.
        """

        for key, value in contents.items():
            if isinstance(value, list):
                contents[key] = self._format_lsit(value, [])
            elif isinstance(value, dict):
                contents[key] = self._format_dict(value, [])
            elif isinstance(value, str):
                contents[key] = [self._format_str(value)]
            else:
                contents[key] = [value]

    def _format_list(self, content, elements):
        """Fomart list's values recursively.

        Parameters
        ----------
        content: list
            The target to format.
        elemetns: list
            The list to be appended formatted valeus.

        Returns
        -------
        elements: lsit
            The list that contains formatted valeus.

        Raises
        ------
        TypeError:
            If content is not lsit or content values are not dict, list, str or Number.
        """
        if not isinstance(content, list):
            raise TypeError(f"'{content}' is not list")

        elements.append('[')
        for value in content:
            if isinstance(value, dict):
                self._format_dict(value, elements)
            elif isinstance(value, list):
                self._format_list(value, elements)
            elif isinstance(value, str):
                elements.append(self._format_str(value))
            elif isinstance(value, Number):
                elements.append(str(value))
            else:
                raise TypeError(f"Type of '{value}' is invalid, got: {type(value)}")
        elements.append(']')

        return elements

    def _format_dict(self, content, elements):
        """Fomart dict's values recursively.

        Parameters
        ----------
        content: dict
            The target to format.
        elemetns: list
            The list to be appended formatted valeus.

        Returns
        -------
        elements: lsit
            The list that contains formatted valeus.

        Raises
        ------
        TypeError:
            If content is not dict or content values are not dict, list, str or Number.
        """
        if not isinstance(content, dict):
            raise TypeError(f"'{content}' is not dict")

        elements.append('{')
        for value in content.values():
            if isinstance(value, dict):
                self._format_dict(value, elements)
            elif isinstance(value, list):
                self._format_list(value, elements)
            elif isinstance(value, str):
                elements.append(self._format_str(value))
            elif isinstance(value, Number):
                elements.append(str(value))
            else:
                raise TypeError(f"Type of '{value}' is invalid, got: {type(value)}")
        elements.append('}')

        return elements

    def _format_str(self, content):
        """Make doubl quoted string.

        Parameters
        ----------
        content: str
            String to be double quoted.

        Returns
        -------
        Double quoted string.

        Raises
        ------
        TypeError:
            If content is not str.
        """
        if not isinstance(content, str):
            raise TypeError(f"'{content}' is not str")
        return '"{}"'.format(content)
