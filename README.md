# Ironsworn AssetsBuilder

AssetBuilder is a cli that allows creating custom asset cards.

### Usage

To start, install the package locally with:

```bash
pip install .
```

to watch the changes as you edit the config file, use:

```bash
assetBuilder watch ./example.json
# or
assetBuilder watch ./example.yaml
```

to build a final html file, use:

```bash
assetBuilder build ./example.json
```

You can also build a printable pdf or an image of each asset. Use the `--help` flag to learn more.

### Credits

This work is inspired by Ironsworn (found at www.ironswornrpg.com), created by Shawn Tomkin, and licensed for our use under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International license (creativecommons.org/licenses/by-nc-sa/4.0/).

Some of the css and visuals are taken from [Asset Workbench](https://effortlessmountain.github.io/ironsworn-asset-workbench/)
