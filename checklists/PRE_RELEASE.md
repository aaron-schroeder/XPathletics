# Pre-release checklist

You are about to release the latest version.
Here's a list of things not to forget.

* [Changelog page](../docs/source/whatsnew/) for this version
  * Created
  * Has entries for each change I made since last version
  * Any remaining boilerplate text is removed
  * Has the release date included ("??" replaced)
  * Previewed by running `make doc` and viewing 
    [HTML docs](../docs/_build/html) in browser.

* [`__version__`](../adspackage/__init__.py) updated appropriately from
  [latest release on PyPi](https://pypi.org/project/adspackage/).

* Run tests one last time with `make test`. The package will have
  been tested with GH actions during each pull request, so *theoretically*
  this is redundant.

## Release template

Create a new release on GitHub, name it "adspackage {major}.{minor}.{patch}"
and create the tag "v{major}.{minor}.{patch}".

If not inspired to write more after the changelog, refer to it in the comment
when creating the new release:

```markdown
See the [full whatsnew](https://adspackage.readthedocs.io/en/latest/source/whatsnew/v{major}.{minor}.{patch}.html)
for a list of all the changes.
```

