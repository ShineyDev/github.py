"""
/github/objects/topic.py

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

from github.abc import Node
from github.abc import Type


class Topic(Node, Type):
    """
    Represents a GitHub topic.

    Implements:

    * :class:`~github.abc.Node`
    * :class:`~github.abc.Type`
    """

    # https://docs.github.com/en/graphql/reference/objects#topic

    __slots__ = ("data", "http")

    def __init__(self, data, http):
        self.data = data
        self.http = http

    def __repr__(self):
        return "<{0.__class__.__name__} name='{0.name}'>".format(self)

    @property
    def name(self):
        """
        The topic's name.

        :type: :class:`str`
        """

        return self.data["name"]

    async def fetch_related_topics(self):
        """
        Fetches a list of up to 10 related topics.

        Returns
        -------
        List[:class:`~github.Topic`]
            A list of topics.
        """

        data = await self.http.fetch_topic_related_topics(self.id)
        return Topic.from_data(data, self.http)
