from moviepy.editor import VideoFileClip, concatenate_videoclips
def merge_videos(video_files, output_file):
    # Videoları yükle
    clips = [VideoFileClip(video) for video in video_files]
    # Videoları birleştir
    final_clip = concatenate_videoclips(clips)
    # Sonuç dosyasını kaydet
    final_clip.write_videofile(output_file, codec="libx264")
if __name__ == "__main__":
    # Birleştirmek istediğin videoların dosya adlarını buraya ekle
    video_files = ["/home/berhan/Downloads/ilk_kısım.mp4", "C://Users//Umut//Desktop//segment//output_video6.mp4"]
    # Çıktı dosyasının adı
    output_file = "output.mp4"
    merge_videos(video_files, output_file)