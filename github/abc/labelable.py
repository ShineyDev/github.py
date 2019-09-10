"""
/github/abc/labelable.py

    Copyright (c) 2019 ShineyDev
    
    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

import typing


class Labelable():
    """
    Represents an object which can be labeled.

    https://developer.github.com/v4/interface/labelable/
    """

    __slots__ = ()

    async def fetch_labels(self) -> typing.List["Label"]:
        """
        |coro|

        Fetches a list of labels from this labelable.

        Raises
        ------
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The labelable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        """

        # prevent cyclic imports
        from github.objects import Label

        data = await self.http.fetch_labelable_labels(self.id)
        return Label.from_data(data, self.http)
        
    async def add_labels(self, *labels: "Label"):
        """
        |coro|

        Adds labels to the labelable.

        Parameters
        ----------
        \\*labels: Iterable[:class:`github.Label`]
            An iterable of labels.

        Raises
        ------
        ~github.errors.Forbidden
            You don't have permission to add labels.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The labelable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        """

        labels = [label.id for label in labels]
        await self.http.add_labels(self.id, labels)

    async def clear_labels(self):
        """
        |coro|

        Clears all labels from the labelable.

        Raises
        ------
        ~github.errors.Forbidden
            You don't have permission to clear labels.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The labelable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        """

        await self.http.clear_labels(self.id)

    async def remove_labels(self, *labels: "Label"):
        """
        |coro|

        Removes labels from the labelable.

        Parameters
        ----------
        \\*labels: Iterable[:class:`github.Label`]
            An iterable of labels.

        Raises
        ------
        ~github.errors.Forbidden
            You don't have permission to remove labels.
        ~github.errors.Internal
            A ``"INTERNAL"`` status-message was returned.
        ~github.errors.NotFound
            The labelable does not exist.
        ~github.errors.Unauthorized
            Bad credentials were given.
        ~github.errors.HTTPException
            An arbitrary HTTP-related error occurred.
        ~github.errors.GitHubError
            An arbitrary GitHub-related error occurred.
        """

        labels = [label.id for label in labels]
        await self.http.remove_labels(self.id, labels)
