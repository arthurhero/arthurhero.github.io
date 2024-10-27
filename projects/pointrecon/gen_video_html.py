import glob

temp = "    <div class=\"container is-centered\" id=\"scene0707_00\">\n      <video id=\"scene0707_00\" controls muted height=\"100%\">\n        <source src=\"https://huggingface.co/arthurhero/pointrecon_stuff/resolve/main/videos/scene0707_00.mp4\"\n        type=\"video/mp4\">\n      </video>\n      <h4 class=\"subtitle has-text-centered\">\n              scene0707_00\n      </h4>\n    </div>\n"

print(temp)

scenes = glob.glob("pointrecon_stuff/videos/*mp4")
scenes = sorted(scenes)
text = ""
for scene in scenes:
    scene_name = scene.split('/')[-1].split('.')[0]
    print(scene_name)
    html_text = temp.replace("scene0707_00", scene_name)
    text += html_text

with open("videos.html", 'w') as f:
    f.write(text)
    f.close()
