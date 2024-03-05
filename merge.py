from moviepy.editor import concatenate_audioclips, AudioFileClip
from pydub import AudioSegment

def read_text_from_file(file):
  if file.split('.')[1]=="txt":
    with open(file) as f:
        contents = f.readlines()
    return contents

cnt1 = read_text_from_file("first_mp3.txt")
cnt1 = [t.replace('\n', '') for t in cnt1]



cnt2=read_text_from_file("second_mp3.txt")
cnt2 = [t.replace('\n', '') for t in cnt2]



def segment(s1,e1,s2,e2):
    if len(cnt1)<=len(cnt2):
        for i in range(len(cnt1)):
            print(cnt1[i])
            input_audio1 = AudioFileClip(cnt1[i])
            
            input_audio2 = AudioFileClip(cnt2[i])

            seg1=input_audio1.subclip(s1, e1)
            seg2=input_audio2.subclip(s2, e2)

            final_audio = concatenate_audioclips([seg1, seg2])
            
            final_audio.write_audiofile(f"output{i}.mp3")
            print("output" , i,"  is created successfully")


    else:
        for i in range(len(cnt2)):
            print(i)
            input_audio1 = AudioFileClip(cnt1[i])
            input_audio2 = AudioFileClip(cnt2[i])

            seg1=input_audio1.subclip(s1, e1)
            seg2=input_audio2.subclip(s2, e2)

            final_audio = concatenate_audioclips([seg1, seg2])
            
            final_audio.write_audiofile(f"output{i}.mp3")
            print("output" , i,"  is created successfully")



def segment2(s1,e1,s2,e2,s3,e3):
    if len(cnt1)<=len(cnt2):
        for i in range(len(cnt1)):
            print(cnt1[i])
            input_audio1 = AudioFileClip(cnt1[i])
            
            input_audio2 = AudioFileClip(cnt2[i])

            input_audio3 = AudioFileClip(cnt1[i])

            seg1=input_audio1.subclip(s1, e1)
            seg2=input_audio2.subclip(s2, e2)
            seg3=input_audio1.subclip(s3, e3)

            final_audio = concatenate_audioclips([seg1, seg2, seg3])
            
            final_audio.write_audiofile(f"output{i}.mp3")
            print("output" , i,"  is created successfully")


    else:
        for i in range(len(cnt2)):
            print(i)
            input_audio1 = AudioFileClip(cnt1[i])
            input_audio2 = AudioFileClip(cnt2[i])

            seg1=input_audio1.subclip(s1, e1)
            seg2=input_audio2.subclip(s2, e2)

            final_audio = concatenate_audioclips([seg1, seg2])
            
            final_audio.write_audiofile(f"output{i}.mp3")
            print("output" , i,"  is created successfully")
           





if __name__ == '__main__':
    print("1- specific second\n",'2- med mp3')
    number=input()
    if number=="1":
        print("enter the start second of 1st file \n")
        s1= input()
        print("enter the end second of 1st file \n")
        e1= input()
        print("enter the start second of 2nd file \n")
        s2= input()
        print("enter the end second of 2nd file \n")
        e2= input()
        call = segment(s1,e1,s2,e2)
    elif number=="2":
        
        print("enter the start second of 1st file \n")
        s1= input()
        print("enter the end second of 1st file \n")
        e1= input()
        print("enter the start second of 2nd file \n")
        s2= input()
        print("enter the end second of 2nd file \n")
        e2= input()
        
        print("enter the 2nd start second of 1st file \n")
        s3= input()
        print("enter the 2nd end second of 1st file \n")
        e3= input()
        call = segment2(s1,e1,s2,e2,s3,e3)
          
        
