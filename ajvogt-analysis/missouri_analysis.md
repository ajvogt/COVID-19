# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 07/27/2020  
Source: [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19)  
Source Code: `/ajvogt-analysis/mo_analysis_script.py`  
[Release Notes found below](#release-notes)

This analysis shows the Johns Hopkins University COVID-19 data broken down by 
[Metropolitan Statistcal Area](https://en.wikipedia.org/wiki/Metropolitan_statistical_area) (MSA)
 combinations within the state of Missouri. The list of counties in each MSA comibination can be found in the 
[table](#msa-counties) 
below. The [detailed map of MSAs](https://www2.census.gov/geo/maps/metroarea/us_wall/Sep2018/CBSA_WallMap_Sep2018.pdf) 
can be found here.  The clusters used in the charts and tables below 
are a custom combination of MSAs and 
[Combined Statistical Areas](https://en.wikipedia.org/wiki/Combined_statistical_area) (CSA).


## Missouri New Daily Deaths by Metropolitan Statistcal Areas
![](images/mo_daily_deaths.png)

## Missouri New Daily Confirmed Cases by Metropolitan Statistcal Areas
![](images/mo_daily_cases.png)

## Missouri Metropolitan Statistical Area Totals
<!-- msa_table start -->
| MSA | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|
| St. Louis-Farmington | 1181 | 25476 | 717 | 581 | 399 |
| Kansas City | 329 | 18958 | 466 | 417 | 336 |
| Missouri non-MSA | 77 | 6429 | 172 | 159 | 118 |
| Springfield | 12 | 1319 | 55 | 51 | 32 |
| Joplin | 26 | 2245 | 50 | 48 | 49 |
| Columbia-Jefferson City | 8 | 1460 | 49 | 43 | 31 |
| Cape Girardeau-Sikeston | 16 | 891 | 20 | 22 | 18 |
| St. Joseph | 12 | 1161 | 10 | 9 | 8 |
<!-- msa_table end -->

## STL-Farmington MSA New Daily Deaths by County
![](images/stl_daily_deaths.png)

## STL-Farmington MSA New Daily Confirmed Cases by County
![](images/stl_daily_cases.png)

<a name="msa-counties"></a>
## Metropolitan Statistical Area (MSA) Counties
<!-- county_table start -->
| MSA | State | County | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|---|---|
| St. Louis-Farmington | Missouri | St. Louis | 628 | 11210 | 317 | 242 | 166 |
| Kansas City | Missouri | Kansas City | 45 | 4785 | 152 | 119 | 85 |
| St. Louis-Farmington | Missouri | St. Charles | 84 | 2663 | 131 | 94 | 55 |
| Kansas City | Kansas | Johnson | 94 | 4455 | 101 | 106 | 98 |
| Kansas City | Missouri | Jackson | 55 | 2507 | 85 | 65 | 46 |
| St. Louis-Farmington | Missouri | St. Louis City | 164 | 3901 | 71 | 68 | 52 |
| St. Louis-Farmington | Illinois | St. Clair | 153 | 3152 | 61 | 60 | 47 |
| Kansas City | Kansas | Wyandotte | 91 | 4065 | 58 | 72 | 66 |
| St. Louis-Farmington | Illinois | Madison | 71 | 1840 | 51 | 45 | 31 |
| Joplin | Missouri | Jasper | 23 | 1509 | 38 | 35 | 36 |
| St. Louis-Farmington | Missouri | Jefferson | 24 | 954 | 34 | 26 | 17 |
| Springfield | Missouri | Greene | 9 | 859 | 33 | 30 | 19 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 928 | 26 | 25 | 20 |
| Kansas City | Missouri | Cass | 8 | 440 | 24 | 16 | 10 |
| Missouri non-MSA | Missouri | Camden | 3 | 203 | 14 | 8 | 4 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 447 | 13 | 12 | 8 |
| Kansas City | Missouri | Clay | 19 | 717 | 13 | 11 | 10 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 3 | 521 | 13 | 13 | 12 |
| Joplin | Missouri | Newton | 3 | 736 | 12 | 13 | 13 |
| Kansas City | Kansas | Leavenworth | 7 | 1337 | 12 | 8 | 6 |
| Missouri non-MSA | Missouri | Pettis | 3 | 274 | 11 | 9 | 5 |
| Missouri non-MSA | Missouri | Taney | 3 | 249 | 10 | 9 | 6 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 221 | 9 | 7 | 4 |
| Columbia-Jefferson City | Missouri | Cole | 2 | 226 | 9 | 8 | 5 |
| Springfield | Missouri | Polk | 0 | 150 | 9 | 9 | 4 |
| Missouri non-MSA | Missouri | McDonald | 7 | 882 | 9 | 12 | 13 |
| Missouri non-MSA | Missouri | Johnson | 1 | 417 | 9 | 12 | 10 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 90 | 8 | 4 | 2 |
| Springfield | Missouri | Christian | 1 | 172 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 3 | 194 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Butler | 2 | 192 | 6 | 5 | 3 |
| Kansas City | Missouri | Platte | 6 | 252 | 6 | 7 | 4 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 234 | 6 | 4 | 3 |
| St. Joseph | Missouri | Buchanan | 10 | 1017 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 136 | 6 | 5 | 3 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 285 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Marion | 1 | 85 | 5 | 3 | 2 |
| St. Louis-Farmington | Missouri | Warren | 0 | 120 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Howell | 0 | 98 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Laclede | 1 | 171 | 4 | 6 | 4 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 224 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Barry | 0 | 188 | 4 | 6 | 5 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 298 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 131 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Audrain | 1 | 182 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Carroll | 0 | 71 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Saline | 6 | 369 | 3 | 4 | 2 |
| Kansas City | Kansas | Miami | 0 | 92 | 3 | 2 | 2 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 109 | 3 | 2 | 2 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 93 | 3 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 37 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 122 | 3 | 1 | 1 |
| Springfield | Missouri | Webster | 1 | 97 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Stone | 1 | 58 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Douglas | 1 | 46 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 189 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Miller | 0 | 62 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Pemiscot | 6 | 179 | 2 | 4 | 2 |
| Missouri non-MSA | Missouri | Benton | 0 | 51 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 50 | 2 | 1 | 1 |
| Kansas City | Missouri | Clinton | 0 | 53 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 171 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 0 | 32 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Morgan | 0 | 45 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 94 | 2 | 2 | 1 |
| Springfield | Missouri | Dallas | 1 | 41 | 1 | 1 | 0 |
| St. Louis-Farmington | Illinois | Bond | 2 | 38 | 1 | 1 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 43 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Adair | 0 | 119 | 1 | 1 | 1 |
| Kansas City | Missouri | Ray | 0 | 48 | 1 | 1 | 0 |
| Kansas City | Missouri | Bates | 1 | 29 | 1 | 1 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 50 | 1 | 2 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 74 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 38 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Henry | 3 | 50 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 36 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 21 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 1 | 44 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 0 | 40 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 29 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Perry | 3 | 187 | 1 | 1 | 2 |
| Kansas City | Missouri | Caldwell | 1 | 27 | 1 | 0 | 0 |
| Kansas City | Missouri | Lafayette | 2 | 125 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 1 | 54 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 37 | 1 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 27 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 12 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 13 | 1 | 0 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 59 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 31 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Washington | 1 | 46 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Crawford | 0 | 34 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 15 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 53 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Texas | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 74 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 45 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 54 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Shelby | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 39 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 10 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 124 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Phelps | 0 | 59 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Oregon | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 2 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 2 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 0 | 4 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 13 | 0 | 0 | 0 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
* 7/20/2020:
  * update table insertion code
  * fix cases vs. deaths total header bug
  * include MSA totals table
  * added STL-Farmington County-level Deaths & Cases plots
  * including release notes in missouri_analysis.md
* 7/19/2020: 
  * code refactor
  * updating color scheme for plots
  * updating county numbers to table to include
  latest new daily case average numbers and
  sorting by last 7-day average
* 6/19/2020: Added description of MSAs & CSAs
* 6/16/2020: Including individual county totals (only) in analysis md table
* 6/11/2020:
  * Updated MSA definitions
  * Including table of individual county case counts
* 6/7/2020: Creating markdown & script
  * Including list of county-MSA/CSA associations to markdown
  * Including cumulative totals in MSA/CSA plots
* 5/30/2020: including plots of cumulative cases/deaths in jupyter notebook
* 5/17/2020: Initial analysis jupyter notebook created
* 4/4/2020: Cloned JHU CSSE Repository and set up development environment

### To-Do (updated 7/20/2020)

#### Analysis Page
- [ ] Update description to accurately reflect CSA vs. MSA
- [x] Make table for CSA info
- [x] Include 7, 14, & 30 day changes for each county
- [ ] Plot top CSAs (for latest daily case change) with testing data
- [x] Analysis breakdown of St. Louis-Farmington counties
- [x] Include release notes and to-do list
- [ ] ~~Update color scheme~~, plot markers, and line thickness
- [ ] Include table of contents

#### Analysis Script
- [x] Simplify data ingestion and summarization functionality
- [x] Simplify plotting functionality
- [x] Include ability to update markdown with table between markdown sections
