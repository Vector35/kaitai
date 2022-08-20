## Overall Idea

We compile the [Kaitai Struct formats](https://github.com/kaitai-io/kaitai_struct_formats) with the `--debug` flag which puts a `._debug` attribute in each KaitaiStruct object, where we can read the `.start` and `.end` of each identified region of bytes.

Every dissected file becomes a tree, where each node represents an identified region.

This tree is refined, and then converted to QTreeWidgetItem to be displayed in a QTreeWidget. Clicks on items highlight the bytes between `.start` and `.end` in the binaryninjaui.HexEditor.

## Directory Structure

* `./compile-all.py` converts the [Kaitai Struct formats](https://github.com/kaitai-io/kaitai_struct_formats) to python modules
* `./import-all.py` test imports all the compiled format modules (generated by compile-all.py)
* `./formats` a [python package](https://docs.python.org/3/tutorial/modules.html) to hold all the Kaitai formats compiled to python modules
* `./formats/__init__.py` promoting the directory to a package
* `./corelogic/kaitaistruct.py` the kaitaistruct runtime (also via `pip install kaitaistruct`)
* `./corelogic/kshelpers.py` main code
* `./plugin` code to hook up with BinaryNinja UI
* `./media` screenshots for the README

QT and BinaryNinja and BinaryNinja UI stuff is intentionally kept isolated within `./plugin` so that rapid development and commandline testing can be performed.

## Tree Forms

After Kaitai parses a file, you get some object that extends `kaitaistruct.KaitaiStruct`. Its attributes refer to either other `kaitaistruct.KaitaiStruct` or primitives like ints. In this way, the parsed data structure is like a tree, with primitives at the leaves.

There are a few undesirable properties of this tree:

* fields can have a `MyFieldName` form or `_m_MyFieldName` form.
* field start/end are sometimes absolute in the file, and sometimes relative to their parent
* parents hold info on their children (name, start, end)

For this reason, we refine this tree to one where:

* fields are always of the `MyFieldName` form
* field start/end are always absolute int he file
* all nodes know their own name, start, end

See TreeNode and `build_tree()`.

The final form, just prior to UI display, is a QTreeItem form.

## Absolute vs. Relative Offsets

Kaitai sometimes sets `.start` and `.end` to offsets within the target file. But other times it's offsets within a buffer, rebasing `.start` and `.end` to 0. Here's an example from microsoft_pe:

```python
    self._raw_optional_hdr = self._io.read_bytes(self.coff_hdr.size_of_optional_header)
    _io__raw_optional_hdr = KaitaiStream(BytesIO(self._raw_optional_hdr))
    self.optional_hdr = MicrosoftPe.OptionalHeader(_io__raw_optional_hdr, self, self._root)
    self.optional_hdr._read()
    self._debug['optional_hdr']['end'] = self._io.pos()
    self._debug['sections']['start'] = self._io.pos()
```

The buffer `_io__raw_optional_hdr` is read from the file IO, and wrapped in a new IO.

A primitive method to do this is to descend thru the tree and push deltas downward. See `normalize_offsets()`.

## Compiled formats in a package

The compiled formats are in their own package called formats, like:

```
./formats/__init__.py
./formats/elf.py
./formats/mach_o.py
...
```

The reason is because the compiled formats use intra-package imports, like `from . import windows_systemtime` or `from . import ethernet_frame`. Obviously this won't work without a package set, and that requires two ingredients: the package directory structure with `__init__.py` existing and variable`__package__` being set at the time the intra-package import occurs. The `__package__` is usually set with statements like `from MyPackage import MyFormat` or `import MyPackage.MyFormat`.

Since we load the formats dynamically (to avoid statically executing `from formats import MyFormat` for every single format), we have to set the python module path carefully. We add the repository directory to the module path, so that `formats` is an immediate subdirectory and a `importlib.import_module()` call can specify `formats.MyFormat` to set the package.

See `ksImportClass()` for implementation details.