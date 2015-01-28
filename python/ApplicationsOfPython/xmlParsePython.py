import xml.dom.minidom

def main():

	doc=xml.dom.minidom.parse("sampleXML.xml")
	
	print("Node name:",doc.firstChild.tagName)
	
	skills = doc.getElementsByTagName("skill")
	print("%d skills: " % skills.length)

	counter = 0
	for skill in skills:
		print("Skill #",counter,"-",skill.getAttribute("name"))
		counter+=1
		
	newSkill = doc.createElement("skill")
	newSkill.setAttribute("name","javascript")
	doc.firstChild.appendChild(newSkill)
	
	skills = doc.getElementsByTagName("skill")
	print( "%d skills: " % skills.length)

	counter = 0
	for skill in skills:
		print("Skill #",counter,"-",skill.getAttribute("name"))
		counter+=1
		
main()
