from docxtpl import DocxTemplate
tpl = DocxTemplate("C:\\Users\\harsh\\Desktop\\hacky\\template.docx")
context = {'TITLE':'Hello',
            'SUB_H_1':#subheading 1,
            'SUB_H_2':#subheading 2,
            'SUB_H_3':#subheading 2,
            'ins_txt1':#summary 1,
            'ins_txt2':#summary 2,
            'ins_txt3':#summary 3,}
            
            
old_image1 ="Picture 714051881"
old_image2 = "Picture 681287327"
old_image3 ="Picture 779674354"

new_image1 = #image path
new_image2 = #image path
new_image3 = #image path
tpl.replace_pic(old_image1,new_image1)
tpl.replace_pic(old_image2,new_image2)
tpl.replace_pic(old_image3,new_image3)
tpl.render(context)
tpl.save("Fianl_template.docx")

