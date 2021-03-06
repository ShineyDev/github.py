"""
/github/abc/deletable.py

    Copyright (c) 2019-2020 ShineyDev

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

class Deletable():
    """
    Represents an object which can be deleted.

    Implemented by:

    * :class:`~github.CommitComment`
    """

    # https://docs.github.com/en/graphql/reference/interfaces#deletable

    __slots__ = ()

    @property
    def viewer_can_delete(self):
        """
        Whether the authenticated user can delete the deletable.

        :type: :class:`bool`
        """

        return self.data["viewerCanDelete"]

    async def delete(self):
        """
        |coro|

        Deletes the deletable.

        Raises
        ------
        ~github.errors.Forbidden
            You do not have permission to delete the deletable.
        """

        ...
