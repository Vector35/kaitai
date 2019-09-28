# Kaitai Struct Binary Ninja Plugin

Author: Vector 35 Inc

This UI plugin allows you to browse a hex dump within Binary Ninja with a tree view informed by [Kaitai Struct](https://kaitai.io/).

![](./media/kaitai.gif)

## Description:

This wires up Kaitai Struct as a parsing library to produce templated dissection of binary files. Of course, this concept itself isn’t new. Plenty of great tools like 010, Hexinator and Synalyze It! have this feature (last two by the same company for different platforms). Thanks to the Kaitai Project not only for the project in general, but also for working with us to resolve some small issues while we were developing the plugin.

## Required Dependencies

There are no external dependencies for this plugin. All of the Kaitai formats are precompiled to Python for self-contained use.

## License

This plugin is released under a [MIT](https://github.com/Vector35/snippets/blob/master/LICENSE) license.