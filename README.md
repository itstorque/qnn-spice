# qnn-spice
QNN's SPICE models library

This repository sync's all of the SPICE models we use with their respective remotes
and updates the LTSpice internal directory to add a new `[qnn-spice]` folder into
LTSpice's component library that sorts the components.

## Example

<center><img src="example.png" width="350px"/></center>

The component library for the following `models.md` config:

```
- htron_behavioral: htrons
  - htron_behav_model.asc: htron_b.asc
  - htron_behav_model.asy: htron_b.asy
- JJ: JJs
  - JJ.asy: JJ_v1.asy
  - JJ.lib: JJ_v1.lib
- JJ_v2: JJs
  - JJ.asy: JJ_v2.asy
  - JJ.lib: JJ_v2.lib
- ntron: ntron
  - ntron.lib
  - ntron.asy
```


## Usage



## install notes

- `chmod +x update`
- git submodule update
- check update script on windows, might need a separate file...