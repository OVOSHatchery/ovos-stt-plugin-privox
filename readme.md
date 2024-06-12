# Privox STT plugin

A stt plugin for ovos using [Privox](https://privox.io)

> **WARNING**: Unfortunately the Privox network seems to no longer have any active nodes, consider using the [OVOS public servers](https://github.com/OpenVoiceOS/status) if you need volunteer run services for TTS/STT

![image](https://github.com/OVOSHatchery/ovos-stt-plugin-privox/assets/33701864/9f96317d-4874-4c9e-965b-9687d0040237)

_________________

## Install

`pip install ovos-stt-plugin-privox`


## Configuration

By default the global language used by mycroft-core will be used

```json
  "stt": {
    "module": "ovos-stt-plugin-privox",
    "ovos-stt-plugin-privox": {"quality": "fast", "key": "SECRET"}
  }
 
```
