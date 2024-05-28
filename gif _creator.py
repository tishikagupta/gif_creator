from moviepy.editor import ImageSequenceClip

#image_files=[]
#image_clips=ImageSequenceClip(image_files,fps=24)
#gif_path="output.gif"
#image_clips.write_gif(gif_path)


def create_gif(image_files, gif_path, fps=10):
    if not image_files:
        print("error")
        return
    image_clips= ImageSequenceClip(image_files, fps=fps)
    image_clips.write_gif(gif_path,fps=fps)

if __name__ == "__main__":
    image_files = ['imag1.png', 'image2.png', 'imag3.png']  
    gif_path = 'output.gif'
    create_gif(image_files, gif_path)