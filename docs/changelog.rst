.. currentmodule:: github


Changelog
=========

v0.4.0
------

Bug Fixes
~~~~~~~~~

* Fix node subclass equality.

New Features
~~~~~~~~~~~~

* Implement :class:`github.Issue`.
* Implement :class:`github.Label`.
* Implement :class:`github.PullRequest`.
* Implement :class:`github.abc.Assignable`.
* Implement :class:`github.abc.Closable`.
* Implement :class:`github.abc.Commentable`.
* Implement :class:`github.abc.Labelable`.
* Implement :class:`github.abc.Lockable`.
* Implement :class:`github.abc.Participable`.
* Implement :class:`github.enums.IssueState`.
* Implement :class:`github.enums.LockReason`.
* Implement :class:`github.enums.PullRequestState`.
* Implement :attr:`github.query.Fragment.inline`.
* Implement :class:`github.query.Query`.
* Implement :class:`github.query.Mutation`.

Updated Features
~~~~~~~~~~~~~~~~

* The default user agent now contains a `random UUID <https://docs.python.org/3/library/uuid.html#uuid.uuid4>`_.
* :exc:`TypeError` is now raised when passing an invalid type to ``github.query.*.add_*`` methods.


v0.3.3
------

New Features
~~~~~~~~~~~~

* Implement :class:`github.CodeOfConduct.resource_path`
* Implement :class:`github.abc.Subscribable`

Updated Features
~~~~~~~~~~~~~~~~

* :class:`github.Repository` now subclasses :class:`github.abc.Subscribable`.


v0.3.2
------

Bug Fixes
~~~~~~~~~

* Fix :func:`github.utils.get` returning multiple of the same object even if it doesn't match all attributes.

New Features
~~~~~~~~~~~~

* Implement :func:`github.utils.find_all`.
* Implement :func:`github.utils.find`.
* Implement :func:`github.utils.get_all`.


v0.3.1
------

Bug Fixes
~~~~~~~~~

* Fix typing in :class:`github.http.HTTPClient`.

New Features
~~~~~~~~~~~~

* Implement :class:`github.abc.ProfileOwner`.
* Implement :class:`github.abc.ProjectOwner`.
* Implement :class:`github.abc.Type`.
* Implement :class:`github.abc.UniformResourceLocatable`.
* Implement :meth:`github.GitHub.fetch_organization`.
* Implement :class:`github.Organization`.
* Implement :meth:`github.GitHub.fetch_scopes`.

Removed Features
~~~~~~~~~~~~~~~~

* Remove typing from ``from_data`` and ``__init__`` non-user facing methods.


v0.3.0
------

New Features
~~~~~~~~~~~~

* Implement :meth:`github.query.Builder.from_dict`.
* Implement :meth:`github.query.Builder.to_dict`.
* Implement :meth:`github.query.Builder.copy`.
* Implement :meth:`github.query.Collection.from_dict`.
* Implement :meth:`github.query.Collection.to_dict`.
* Implement :meth:`github.query.Collection.copy`.
* Implement :meth:`github.query.CollectionArgument.from_dict`.
* Implement :meth:`github.query.CollectionArgument.to_dict`.
* Implement :meth:`github.query.CollectionArgument.copy`.
* Implement :meth:`github.query.Field.from_dict`.
* Implement :meth:`github.query.Field.to_dict`.
* Implement :meth:`github.query.Field.copy`.
* Implement :meth:`github.query.Fragment.from_dict`.
* Implement :meth:`github.query.Fragment.to_dict`.
* Implement :meth:`github.query.Fragment.copy`.
* Implement :meth:`github.query.QueryArgument.from_dict`.
* Implement :meth:`github.query.QueryArgument.to_dict`.
* Implement :meth:`github.query.QueryArgument.copy`.
* Implement :class:`github.query.Fragment`.
* Implement :meth:`github.query.Builder.add_fragment`.
* Implement :meth:`github.query.Collection.add_fragment`.


v0.2.3
------

Bug Fixes
~~~~~~~~~

* Properly handle :mod:`aiohttp` exceptions. (:issue:`5`)

New Features
~~~~~~~~~~~~

* Implement :meth:`github.GitHub.fetch_codes_of_conduct`.


v0.2.2
------

Bug Fixes
~~~~~~~~~

* Fix typehints. (this should now allow linters and IDEs to work correctly)


v0.2.1
------

Bug Fixes
~~~~~~~~~

* Fix :attr:`github.Repository.license` AttributeError.
* Fix :meth:`github.query.Collection.build` IndexError.


v0.2.0
------

New Features
~~~~~~~~~~~~

* Add :mod:`github.enums`.
* Implement :class:`github.CommitComment`.
* Implement :class:`github.Reaction`.
* Implement :meth:`github.User.fetch_commit_comments`.
* Implement :class:`github.abc.Comment`.
* Implement :class:`github.abc.Deletable`.
* Implement :class:`github.abc.Reactable`.
* Implement :class:`github.abc.RepositoryNode`.
* Implement :class:`github.abc.Updatable`.
* Implement :class:`github.enums.CannotUpdateReason`.
* Implement :class:`github.enums.CommentAuthorAssociation`.
* Implement :class:`github.enums.Reaction`.

Removed Features
~~~~~~~~~~~~~~~~

* Remove ``cache`` kwarg from :meth:`github.abc.Actor.fetch_avatar_url`.

Updated Features
~~~~~~~~~~~~~~~~

* Move ``github/objects/abc/`` to ``github/abc/``.
* Move ``github/objects/repositorylockreason`` to ``github/enums/repositorylockreason``.
* Move ``github/objects/repositorypermissions`` to ``github/enums/repositorypermissions``.
* Move ``github/objects/repositorysubscription`` to ``github/enums/repositorysubscription``.


v0.1.3
------

Bug Fixes
~~~~~~~~~

* Add ``author`` and ``license`` metadata for pip. (:issue:`3`)

Removed Features
~~~~~~~~~~~~~~~~

* Remove ``github.User.email``.

Updated Features
~~~~~~~~~~~~~~~~

* Update exception system.


v0.1.2
------

Bug Fixes
~~~~~~~~~

* Make ``json`` kwarg required in :meth:`~github.http.HTTPClient.request`.

New Features
~~~~~~~~~~~~

* Add ``session`` kwarg to :class:`github.GitHub`.

Updated Features
~~~~~~~~~~~~~~~~

* Update exception system.


v0.1.1
------

Bug Fixes
~~~~~~~~~

* Fix ``python_requires``.


v0.1.0
------

The first official version of the wrapper.

Bug Fixes
~~~~~~~~~

* Add ``objects`` and ``abc`` to packages.
* Fix version regex.

New Features
~~~~~~~~~~~~

* Implement ``__main__`` for ``py -m github --version``.


< v0.1.0
--------

Features and bug fixes before v0.1.0 were not documented.
