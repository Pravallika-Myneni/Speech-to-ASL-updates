from moviepy.editor import *

clip1 = VideoFileClip("C:\\Users\\Pravallika Myneni\\Desktop\\Work\\Personal-Projects\\Speech_to_ASL\\assets\\0.mp4")
clip2 = VideoFileClip("C:\\Users\\Pravallika Myneni\\Desktop\\Work\\Personal-Projects\\Speech_to_ASL\\assets\\1.mp4")

final = concatenate_videoclips([clip1, clip2])
final.write_videofile("Answer.mp4")