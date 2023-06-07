import PIL
import textwrap
from shutil import make_archive
import random
from PIL import Image, ImageFont, ImageDraw
import gradio as gr



def igc(content_title='content_title',
        account_name ='@' + 'a n a l y s e r__s t u d i o',
        sub_title='Add sample text Here',
        sub_title_explanation='This text is an example that helps you explain the subtopic in more detail. You have the chance to provide additional information and give a clear explanation of the subtopic. Use this opportunity to share your knowledge and insights, and help the reader understand the subtopic better.',
        sub_title2='Add sample text Here',
        sub_title_explanation2='This text is an example that helps you explain the subtopic in more detail. You have the chance to provide additional information and give a clear explanation of the subtopic. Use this opportunity to share your knowledge and insights, and help the reader understand the subtopic better.',
        sub_title3='Add sample text Here',
        sub_title_explanation3='This text is an example that helps you explain the subtopic in more detail. You have the chance to provide additional information and give a clear explanation of the subtopic. Use this opportunity to share your knowledge and insights, and help the reader understand the subtopic better.',
        sub_title4='Add sample text Here',
        sub_title_explanation4='This text is an example that helps you explain the subtopic in more detail. You have the chance to provide additional information and give a clear explanation of the subtopic. Use this opportunity to share your knowledge and insights, and help the reader understand the subtopic better.',
        sub_title5='Add sample text Here',
        sub_title_explanation5='This text is an example that helps you explain the subtopic in more detail. You have the chance to provide additional information and give a clear explanation of the subtopic. Use this opportunity to share your knowledge and insights, and help the reader understand the subtopic better.'):


    content_title = content_title
    sub_title = sub_title
    sub_title_explanation = sub_title_explanation
    sub_title2 = sub_title2
    sub_title_explanation2 = sub_title_explanation2
    sub_title3 = sub_title3
    sub_title_explanation3 = sub_title_explanation3
    sub_title4 = sub_title4
    sub_title_explanation4 = sub_title_explanation4
    sub_title5 = sub_title5
    sub_title_explanation5 = sub_title_explanation5

    #Background image list
    titlebg = ['titlebg', 'titlebg1', 'titlebg2', 'titlebg3']
    subbg = ['subbg', 'subbg1', 'subbg2', 'subbg3']
    rntitlebg = random.choice(titlebg)
    rnsubbg = random.choice(subbg)

    #Add Account name on image
    account_name = '@' + 'a n a l y s e r__s t u d i o'
    background_image = Image.open('Background/'+rntitlebg+'.png')
    sub_background_image = Image.open('Background/'+rnsubbg+'.png')
    background_image = background_image.resize((2000 , 2000))
    sub_background_image = sub_background_image.resize((2000 , 2000))
    background_draw = ImageDraw.Draw(background_image)
    sub_background_image_draw = ImageDraw.Draw(sub_background_image)
    account_name_font = ImageFont.truetype('Font/bahnschrift.ttf', 40)
    background_draw.text((56, 1920), account_name.title(), font=account_name_font, fill=(256, 256, 256))
    background_draw.text((1420, 56), account_name.title(), font=account_name_font, fill=(256, 256, 256))
    sub_background_image_draw.text((56, 1920), account_name.title(), font=account_name_font, fill=(256, 256, 256))
    sub_background_image_draw.text((1420, 56), account_name.title(), font=account_name_font, fill=(256, 256, 256))
    background_image.save(f"temp/Title_background.png")
    sub_background_image.save(f"temp/sub_background.png")

    #Add title to image
    new_background_image = Image.open('temp/Title_background.png')
    font_title = ImageFont.truetype('Font/Poppins-SemiBold.ttf', 200)
    new_background_image_draw = ImageDraw.Draw(new_background_image)
    content_title = textwrap.fill(content_title, width=8, break_long_words=False)
    new_background_image_draw.text((420, 420), content_title.upper(), font = font_title, fill=(0, 0, 0))
    new_background_image.save("Result/" + 'Title_Page.png')

    #Making list for content
    sub_title_list = [sub_title, sub_title2, sub_title3, sub_title4, sub_title5]
    sub_title_explanation_list = [sub_title_explanation, sub_title_explanation2, sub_title_explanation3, sub_title_explanation4, sub_title_explanation5]



    sub_title_font = ImageFont.truetype('Font/Poppins-Bold.ttf', 80)
    sub_title_number_font = ImageFont.truetype('Font/Poppins-Bold.ttf', 120)
    sub_title_explanation_font = ImageFont.truetype('Font/Poppins-Medium.ttf', 55)


    for i in range(0,5):
        sub_background_image = Image.open('temp/sub_background.png')
        sub_background_image_draw = ImageDraw.Draw(sub_background_image)
        if len(sub_title_list[i]) < 22:
            sub_title_list[i] = textwrap.fill(sub_title_list[i], width=12, break_long_words=False)
        else:
            sub_title_list[i] = textwrap.fill(sub_title_list[i], width=22, break_long_words=False)
        sub_title_explanation_list[i] = textwrap.fill(sub_title_explanation_list[i], width=35, break_long_words=False)
        sub_background_image_draw.text((450, 520), sub_title_list[i].title(), font= sub_title_font, fill=(0, 0, 0) )
        sub_background_image_draw.text((517, 850), sub_title_explanation_list[i].title(), font=sub_title_explanation_font, fill=(0, 0, 0))
        sub_background_image_draw.text((290, 540), str(i + 1), font=sub_title_number_font,fill=(255, 255, 255))
        sub_background_image.save('Result/' + "Sub_Page" + str(i + 1) + ".png")
    make_archive('Result', 'zip', 'Result')
    return 'Result.zip'



input_title = gr.inputs.Textbox(label="Title")
input_sub_title = gr.inputs.Textbox(label="Subtitle")
input_sub_title_explanation = gr.inputs.Textbox(label="Subtitle Explanation")
input_sub_title2 = gr.inputs.Textbox(label="Subtitle 2")
input_sub_title_explanation2 = gr.inputs.Textbox(label="Subtitle 2 Explanation")
input_sub_title3 = gr.inputs.Textbox(label="Subtitle 3")
input_sub_title_explanation3 = gr.inputs.Textbox(label="Subtitle 3 Explanation")
input_sub_title4 = gr.inputs.Textbox(label="Subtitle 4")
input_sub_title_explanation4 = gr.inputs.Textbox(label="Subtitle 4 Explanation")
input_sub_title5 = gr.inputs.Textbox(label="Subtitle 5")
input_sub_title_explanation5 = gr.inputs.Textbox(label="Subtitle 5 Explanation")

demo = gr.Interface(
    fn=igc,
    inputs=[input_title,input_sub_title,input_sub_title_explanation,input_sub_title2,input_sub_title_explanation2,input_sub_title3,input_sub_title_explanation3,input_sub_title4,input_sub_title_explanation4,input_sub_title5,input_sub_title_explanation5],outputs="file",output_filepath="Result.zip")

demo.launch(inline = False)