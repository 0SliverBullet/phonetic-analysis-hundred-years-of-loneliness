# Phonetic Analysis: Hundred-Years-of-Loneliness

## Overview

This repository is for Phonetic Analysis: Hundred-Years-of-Loneliness, i.e., 《百年孤寂》in Chinese.

We analyzed the following three .mp3 files:

- `audio1.mp3`: [百年孤寂（微醺版）][https://www.bilibili.com/video/BV1gg4y1s7jN/?spm_id_from=333.337.search-card.all.click&vd_source=4264d17960d3662effa4ac3cb6df2e2f]

- `audio2.mp3`: [百年孤寂（吴青峰版）][https://www.bilibili.com/video/BV1hNDdYyEoA/?spm_id_from=333.337.search-card.all.click&vd_source=4264d17960d3662effa4ac3cb6df2e2f]

- `audio3.mp3`: [百年孤寂（王菲版）][https://www.bilibili.com/video/BV1sZ4y1R7V5/?spm_id_from=333.337.search-card.all.click&vd_source=4264d17960d3662effa4ac3cb6df2e2f]

## File Structure

```shell
phonetic-analysis-hundred-years-of-loneliness/
├── src/                 
│   └── main.py
├── utils/               
│   ├── analysis_utils.py           # analyze time serise (whole)
│   ├── analysis_segment_utils.py   # analyze time serise (segment)
│   └── image_utils.py
├── audio/              
│   ├── audio1.mp3
│   ├── audio2.mp3
│   └── audio3.mp3
├── fig  
└──  requirements.txt
```

## Usage

```shell
python ./src/main.py
```

