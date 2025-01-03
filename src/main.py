import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from utils.analysis_utils import analyze_audio

def main():
    """ 
        analyze the following three .mp3 files:
        - audio1.mp3: [百年孤寂（微醺版）][https://www.bilibili.com/video/BV1gg4y1s7jN/?spm_id_from=333.337.search-card.all.click&vd_source=4264d17960d3662effa4ac3cb6df2e2f]
        - audio2.mp3: [百年孤寂（吴青峰版）][https://www.bilibili.com/video/BV1hNDdYyEoA/?spm_id_from=333.337.search-card.all.click&vd_source=4264d17960d3662effa4ac3cb6df2e2f]
        - audio3.mp3: [百年孤寂（王菲版）][https://www.bilibili.com/video/BV1sZ4y1R7V5/?spm_id_from=333.337.search-card.all.click&vd_source=4264d17960d3662effa4ac3cb6df2e2f]
    """
    file_paths = ['./audio/audio1.mp3', './audio/audio2.mp3', './audio/audio3.mp3']
    titles = ['Audio 1', 'Audio 2', 'Audio 3']

    for file_path, title in zip(file_paths, titles):
        analyze_audio(file_path, title)

if __name__ == "__main__":
    main()
