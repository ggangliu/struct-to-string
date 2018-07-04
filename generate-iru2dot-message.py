#coding=utf-8

#通过minidom解析xml文件

#import xml.dom.minidom as xmldom
import xml.etree.cElementTree as cXmlTree
import os, sys

messageString = ""

def convert_xml_to_string(element):
    global messageString
    if len(element) > 0:
        for child in element:
            if None != child.text and '\n\t\t' != child.text and '\n\t\t\t' != child.text:
                print("[info] " + child.tag, "-----", child.text)
                messageString = messageString + child.text
            convert_xml_to_string(child)

if __name__ == "__main__":
    if (len(sys.argv)) == 2:
        xmlFilePath = os.path.abspath(sys.argv[1].replace("\\", "/"))
    else:
        xmlFilePath = os.path.abspath("qmsg_t.xml").replace("\\", "/")

    print("The xml is： ", xmlFilePath)
    try:
        tree = cXmlTree.parse(xmlFilePath)
        #print("tree type: ", type(tree))
        root = tree.getroot()
    except Exception as e:
        print("Parse % fail." % xmlFilePath)
        sys.exit()

    #print("root type: ", type(root))
    print(40 * "*")
    convert_xml_to_string(root)
    print(40 * "*")
    print("messageString: " + messageString)
    with open('messageString.txt', 'w') as f:
        f.write(messageString)
        f.close()

    os.system("notepad messageString.txt")
    #os.system("pause")