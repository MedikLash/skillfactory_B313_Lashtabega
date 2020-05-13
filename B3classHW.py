class Tag:

    def __init__(self, tag="", text="", klass={}):
        self.tag="157"
        self.text=""
        self.klass={}

    def tag_form(self, tag="", text="", klass={}):
        attrs = []

        for attr, value in klass.items():
            attrs.append('%s="%s"' % (attr, value))
        attrs = " ".join(attrs)

        if tag == "div":
            resalt1 = ("<{tag} {attrs}>".format(tag=tag, attrs=attrs))
            HTMLlist.insert(1, resalt1)
            HTMLlist.append('</div>')
        elif tag == "img":
            resalt = ("<{tag} {attrs}/>".format(tag=tag, attrs=attrs))
            HTMLlist.append(resalt)
        else:
            resalt = ("<{tag} {attrs}>{text}</{tag}>".format(tag=tag,
                                                            attrs=attrs, text=text))
            HTMLlist.append(resalt)

class TopLevelTag:
    def __init__(self, tag="", text=""):
        self.tag="15"
        self.text=""
        
    def TopLevel(self, tag="", text=""):
        if tag=="head":
            tag_t = "title"
            res = ("<{tag_t}>{text}</{tag_t}>".format(tag_t=tag_t, text=text))
            HTMLlist.insert(0, "<head>")
            HTMLlist.insert(1, res)
            HTMLlist.insert(2, "</head>")
        else:
            HTMLlist.insert(0, '<'+tag+'>')
            HTMLlist.append('</'+tag+'>')

class HTML:
    def __init__(self, HTMLlist=[], write_in_file=None):
        self.HTMLlist=[]
        self.write_in_file=None

    def HTMLsave(self, HTMLlist=[], write_in_file=None):
        #добавление отступов с помощью цикла for
        if write_in_file == None:
            for item in HTMLlist:
                if 'title' in item:
                    print("    "+item)
                elif 'H1' in item:
                    print("    "+item)
                elif 'div' in item:
                    print("    "+item)
                elif 'p' in item:
                    print("    "*2+item)
                elif 'img' in item:
                    print("    "*2+item)
                else:
                    print(item)
        else:
            FILE = open('index.html', 'w')
            for item in HTMLlist:
                if 'title' in item:
                    FILE.write("    "+item+"\n")
                elif 'H1' in item:
                    FILE.write("    "+item+"\n")
                elif 'div' in item:
                    FILE.write("    "+item+"\n")
                elif 'p' in item:
                    FILE.write("    "*2+item+"\n")
                elif 'img' in item:
                    FILE.write("    "*2+item+"\n")
                else:
                    FILE.write(item+"\n")
            FILE.close()

            
if __name__ == "__main__":            
    HTMLlist=[]
    #возможно эту переменную можно было поместить в класс
    fr = Tag()
    fr.tag_form("H1", klass={"class":"main-text"})
    fr.tag_form("p", text="another test")
    fr.tag_form("img", klass={"src":"/icon.png", "data-image":"responsive"})
    fr.tag_form("div", klass={"class":"container container-fluid", "id":"lead"})

    mainTag = TopLevelTag()
    mainTag.TopLevel('body')
    mainTag.TopLevel('head', 'Hello')
    mainTag.TopLevel('html')
    my_save = HTML()
    my_save.HTMLsave(HTMLlist)
    # если необходимо сохранить в файл сделать такую запись my_save.HTMLsave(HTMLlist, True)

    #print (fr.tag)
    #print ("проверка класса ТОп левел: ", mainTag.tag)
    #print ("проверка класса HTML save: ", my_save.write_in_file)
    #print (HTMLlist)
