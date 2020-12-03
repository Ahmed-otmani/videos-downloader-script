from pytube import YouTube

def get_video(video_link):
	video = YouTube(video_link)
	resulotion = video.streams.first()
	resulotion.download()


print("\vwelcome to YouTube Diwnloader".center(100, "="))
link = str(input("\venter your video's link: ".title()))
permission = str(input("\ndo you want to download it now (Y/n)? "))

if permission == 'y' or permission == 'Y':
	get_video(link)
else: 
	print("download canceled!")



input('\v\vclick enter to exit....'.upper())