from PIL import Image

def combine_audio_images(analysises):
    for analysis in analysises:
        try:
            img1 = Image.open(f'./fig/audio1/{analysis}_Audio1.png')
            img2 = Image.open(f'./fig/audio2/{analysis}_Audio2.png')
            img3 = Image.open(f'./fig/audio3/{analysis}_Audio3.png')

            width1, height1 = img1.size
            width2, height2 = img2.size
            width3, height3 = img3.size

            assert height1 == height2 == height3, "picture height is inconsistent!"
            assert width1 == width2 == width3, "picture width is inconsistent!"

            total_width = width1
            total_height = height1 + height2 + height3


            new_img = Image.new('RGBA', (total_width, total_height))
            new_img.paste(img1, (0, 0)) 
            new_img.paste(img2, (0, height1))  
            new_img.paste(img3, (0, height1 + height2))  
            new_img.save(f'./fig/audios/{analysis}.png')

            print(f"{analysis} combined and saved successfully!")

        except Exception as e:
            print(f"Error processing {analysis}: {e}")

def main():
    analysises = ['Waveform', 'Frequency_Spectrum', 'Spectrogram', 'MFCC', 'Pitch', 'Waveform_Segment1', 'Waveform_Segment2', 'Waveform_Segment3']
    combine_audio_images(analysises)

if __name__ == "__main__":
    main()

