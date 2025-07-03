from moviepy.video.io.VideoFileClip import VideoFileClip

def video_kirp(video_yolu, baslangic_zamani, bitis_zamani, cikis_yolu):
    # Videoyu yükleyin
    video = VideoFileClip(video_yolu)
    
    # Videoyu istenen zaman aralığında kırpın
    kirpilmis_video = video.subclip(baslangic_zamani, bitis_zamani)
    
    # Kırpılmış videoyu kaydedin
    kirpilmis_video.write_videofile(cikis_yolu, codec="libx264", audio_codec="aac")

# Örnek kullanım
video_yolu = "/home/berhan/Desktop/ada_tersanesi/original/ada_4/ADA_SHIPYARD_4.mp4"
baslangic_zamani = "00:00:06"  
bitis_zamani = "00:00:19"      
cikis_yolu = "/home/berhan/Desktop/ada_tersanesi/original/ada_4/ADA_SHIPYARD_4_1.mp4"

video_kirp(video_yolu, baslangic_zamani, bitis_zamani, cikis_yolu)