from datetime import datetime, timedelta
import random

def ContentSections():

    line = "<h2>Headlines</h2>headlines_content"
    line += "<div class='AmazonLink'>headlines_az_content</div>"
    line += "<h2>Independent</h2>independent_content"
    line += "<div class='AmazonLink'>independent_az_content</div>"
    line += "<h2>Republican</h2>republican_content"
    line += "<div class='AmazonLink'>republican_az_content</div>"
    line += "<h2>Democratic</h2>democratic_content"
    line += "<div class='AmazonLink'>democratic_az_content</div>"
    line += "<h2>Analysis and Data</h2>analysis_and_data_content"
    line += "<div class='AmazonLink'>analysisdata_az_content</div>"
    line += "<h2>Polls and Opinion</h2>polls_and_opinion_content"
    line += "<div class='AmazonLink'>pollsopinion_az_content</div>"
    line += "<h2>Regional and Local</h2>region_local_content"
    line += "<div class='AmazonLink'>regionlocal_az_content</div>"
    line += "<h2>International and World</h2>world_content"
    line += "<div class='AmazonLink'>internationalworld_az_content</div>"
    line += "<h2>College and University</h2>college_university_content"
    line += "<div class='AmazonLink'>collegeuniversity_az_content</div>"
    return line

def getLinks(str_filepath):

    cnt = 0
    ret_index = []
    f = open(str_filepath, 'r')
    lines = f.readlines()
    for line in lines:
        if cnt > 0:
            line_items = line.replace("\t","").strip().split("|")
            ret_index.append(line_items)
        cnt = cnt + 1
    f.close()
    ret_index.sort(key=lambda x: x[0].lower())
    return ret_index

def ContentLinks(links):
    
    content_line = ""
    for i in range(0, len(links)):
        content_line += "<h3><a target='_blank' href='" + links[i][2] + "'><b>" + links[i][0] + "</b></a><span class='LinkLineDescription'>&nbsp;&nbsp;&nbsp;&nbsp;" + links[i][1] + "</span></h3>"
    return content_line

def AmazonLinks(links, category):
    
    content_line = ""
    for i in range(0, len(links)):
        if category == links[i][0]:
            content_line += "<div style='padding-bottom: 3px;font-size:9pt;font-color:darkred;'><b>" + links[i][1] + "</b></div>"
            content_line += "<div style='padding-bottom: 3px;font-size:9pt;'><a target='_blank' href='" + links[i][4] + "'><i>" + links[i][2] + "</i></a></div>"
            content_line += "<div style='font-size:8pt;'>" + links[i][3] + "</div>"
            break
    return content_line

headlines_links = getLinks("content/LinksHeadline.csv")
democratic_links = getLinks("content/LinksDemocrat.csv")
amazon_links = getLinks("content/LinksAmazon.csv")
independent_links = getLinks("content/LinksIndependent.csv")
republican_links = getLinks("content/LinksRepublican.csv")
analysis_and_data_links = getLinks("content/LinksAnalysisData.csv")
polls_and_opinion_links = getLinks("content/LinksPollsOpinion.csv")
region_local_links = getLinks("content/LinksRegionLocal.csv")
college_university_links = getLinks("content/LinksCollegeUniversity.csv")
world_links = getLinks("content/LinksWorld.csv")


str_content = ContentSections()
#str_content = DateContent(str_content)
str_content = str_content.replace("headlines_content", ContentLinks(headlines_links)) 
str_content = str_content.replace("headlines_az_content", AmazonLinks(amazon_links, "Headlines")) 
str_content = str_content.replace("democratic_content", ContentLinks(democratic_links)) 
str_content = str_content.replace("democratic_az_content", AmazonLinks(amazon_links, "Democratic")) 
str_content = str_content.replace("independent_content", ContentLinks(independent_links)) 
str_content = str_content.replace("independent_az_content", AmazonLinks(amazon_links, "Independent")) 
str_content = str_content.replace("republican_content", ContentLinks(republican_links)) 
str_content = str_content.replace("republican_az_content", AmazonLinks(amazon_links, "Republican")) 
str_content = str_content.replace("analysis_and_data_content", ContentLinks(analysis_and_data_links)) 
str_content = str_content.replace("analysisdata_az_content", AmazonLinks(amazon_links, "AnalysisData")) 
str_content = str_content.replace("polls_and_opinion_content", ContentLinks(polls_and_opinion_links))
str_content = str_content.replace("pollsopinion_az_content", AmazonLinks(amazon_links, "PollsOpinion")) 
str_content = str_content.replace("region_local_content", ContentLinks(region_local_links)) 
str_content = str_content.replace("regionlocal_az_content", AmazonLinks(amazon_links, "RegionLocal"))
str_content = str_content.replace("college_university_content", ContentLinks(college_university_links))
str_content = str_content.replace("collegeuniversity_az_content", AmazonLinks(amazon_links, "CollegeUniversity"))
str_content = str_content.replace("world_content", ContentLinks(world_links)) 
str_content = str_content.replace("internationalworld_az_content", AmazonLinks(amazon_links, "InternationalWorld"))

with open("index_page_template.html") as i, open("index.html", 'w') as o:
    for line in i:
        line = line.replace("<!-- replace text -->", str_content)
        o.write(line)