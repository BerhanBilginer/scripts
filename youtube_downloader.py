from pytube import YouTube

def youtube_video_indir(video_url, hedef_klasor='.'):
    try:
        # YouTube nesnesini oluştur
        yt = YouTube(video_url)
        
        # En yüksek çözünürlüklü akışı seç
        video = yt.streams.get_highest_resolution()
        
        # Videoyu indir
        print(f"{yt.title} indiriliyor...")
        video.download(output_path=hedef_klasor)
        print("İndirme tamamlandı!")
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    # İndirmek istediğiniz videonun URL'sini girin
    video_url = input("YouTube video URL'sini girin: ")
    
    # Videonun indirileceği klasörü belirleyin (varsayılan olarak geçerli klasör kullanılır)
    hedef_klasor = input("Videonun indirileceği klasörü girin (varsayılan: geçerli klasör): ") or '.'
    
    youtube_video_indir(video_url, hedef_klasor)
