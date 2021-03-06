from typing import Optional, Union

from datetime import datetime

from github.enums import CommentAuthorAssociation
from github.objects import Bot, Mannequin, Organization, User


class Comment():
    @property
    def author(self) -> Union[Bot, Mannequin, Organization, User]: ...
    @property
    def author_association(self) -> CommentAuthorAssociation: ...
    @property
    def body(self) -> str: ...
    @property
    def body_html(self) -> str: ...
    @property
    def body_text(self) -> str: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def created_via_email(self) -> bool: ...
    @property
    def editor(self) -> Optional[Union[User]]: ...
    @property
    def edited_at(self) -> Optional[datetime]: ...
    @property
    def published_at(self) -> datetime: ...
    @property
    def updated_at(self) -> Optional[datetime]: ...
    @property
    def viewer_is_author(self) -> bool: ...
