# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/02/2020  
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
| St. Louis-Farmington | 1215 | 30401 | 822 | 739 | 524 |
| Kansas City | 356 | 22392 | 527 | 514 | 412 |
| Missouri non-MSA | 90 | 7959 | 234 | 202 | 154 |
| Springfield | 13 | 1829 | 78 | 68 | 47 |
| Columbia-Jefferson City | 8 | 1929 | 77 | 59 | 44 |
| Joplin | 31 | 2445 | 32 | 41 | 45 |
| Cape Girardeau-Sikeston | 16 | 1029 | 19 | 20 | 21 |
| St. Joseph | 12 | 1215 | 8 | 9 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 650 | 13162 | 353 | 307 | 216 |
| Kansas City | Missouri | Kansas City | 53 | 5865 | 163 | 164 | 112 |
| Kansas City | Missouri | Jackson | 59 | 3396 | 137 | 113 | 71 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 3508 | 137 | 131 | 80 |
| St. Louis-Farmington | Missouri | St. Louis City | 169 | 4579 | 97 | 88 | 67 |
| Kansas City | Kansas | Johnson | 98 | 5014 | 89 | 96 | 106 |
| St. Louis-Farmington | Illinois | St. Clair | 156 | 3569 | 66 | 65 | 54 |
| St. Louis-Farmington | Missouri | Jefferson | 24 | 1328 | 57 | 45 | 28 |
| St. Louis-Farmington | Illinois | Madison | 72 | 2137 | 53 | 48 | 39 |
| Springfield | Missouri | Greene | 10 | 1204 | 53 | 43 | 30 |
| Kansas City | Kansas | Wyandotte | 95 | 4373 | 45 | 61 | 67 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1205 | 44 | 33 | 27 |
| Kansas City | Missouri | Cass | 9 | 630 | 28 | 27 | 16 |
| Kansas City | Missouri | Clay | 20 | 896 | 27 | 19 | 14 |
| Missouri non-MSA | Missouri | Taney | 3 | 403 | 23 | 16 | 11 |
| Joplin | Missouri | Jasper | 25 | 1646 | 22 | 30 | 34 |
| Missouri non-MSA | Missouri | Pettis | 3 | 407 | 21 | 15 | 9 |
| Springfield | Missouri | Christian | 1 | 275 | 15 | 11 | 7 |
| Missouri non-MSA | Missouri | Camden | 4 | 294 | 15 | 13 | 7 |
| Columbia-Jefferson City | Missouri | Cole | 2 | 307 | 13 | 10 | 7 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 293 | 11 | 10 | 6 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 153 | 11 | 8 | 4 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 3 | 596 | 10 | 12 | 13 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 516 | 10 | 12 | 10 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 297 | 10 | 7 | 4 |
| Kansas City | Missouri | Platte | 10 | 308 | 10 | 7 | 6 |
| Joplin | Missouri | Newton | 6 | 799 | 9 | 11 | 11 |
| Missouri non-MSA | Missouri | Marion | 1 | 150 | 9 | 7 | 4 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 341 | 7 | 7 | 5 |
| Kansas City | Kansas | Leavenworth | 8 | 1392 | 7 | 10 | 7 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 179 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Butler | 2 | 239 | 7 | 6 | 4 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 270 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 184 | 7 | 6 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 242 | 6 | 6 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 91 | 6 | 4 | 2 |
| Missouri non-MSA | Missouri | Johnson | 2 | 463 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | McDonald | 7 | 926 | 6 | 9 | 11 |
| Kansas City | Missouri | Ray | 0 | 90 | 6 | 3 | 2 |
| Missouri non-MSA | Missouri | Saline | 7 | 409 | 5 | 4 | 4 |
| St. Joseph | Missouri | Buchanan | 10 | 1056 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Barry | 0 | 227 | 5 | 5 | 5 |
| St. Louis-Farmington | Missouri | Warren | 0 | 157 | 5 | 5 | 3 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 333 | 5 | 4 | 3 |
| Springfield | Missouri | Polk | 0 | 189 | 5 | 9 | 5 |
| Missouri non-MSA | Missouri | Howell | 2 | 133 | 5 | 5 | 3 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 121 | 4 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 123 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Miller | 0 | 93 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Douglas | 2 | 73 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Randolph | 1 | 55 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Carroll | 0 | 98 | 4 | 3 | 2 |
| Kansas City | Missouri | Lafayette | 2 | 151 | 3 | 2 | 2 |
| Kansas City | Kansas | Miami | 0 | 117 | 3 | 3 | 2 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 131 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 8 | 204 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Laclede | 1 | 194 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Stone | 1 | 82 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 34 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 69 | 2 | 2 | 1 |
| Springfield | Missouri | Webster | 1 | 113 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Benton | 1 | 71 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 62 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Crawford | 0 | 52 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 207 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 0 | 28 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 53 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 134 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Phelps | 0 | 75 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 60 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Perry | 4 | 202 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Macon | 0 | 53 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Pike | 1 | 69 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 0 | 35 | 2 | 1 | 0 |
| St. Louis-Farmington | Illinois | Bond | 2 | 49 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Barton | 0 | 65 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Lewis | 1 | 32 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 13 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Audrain | 1 | 192 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 134 | 1 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 39 | 1 | 1 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 83 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 19 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 179 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 0 | 37 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 45 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 129 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Washington | 1 | 54 | 1 | 1 | 1 |
| Kansas City | Missouri | Clinton | 0 | 61 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Hickory | 0 | 16 | 1 | 1 | 0 |
| Springfield | Missouri | Dallas | 1 | 48 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 17 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 11 | 1 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 56 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 20 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 10 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 65 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 43 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 18 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 79 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 21 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 58 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ripley | 0 | 41 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 6 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 34 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 43 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 6 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 7 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 14 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 17 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 11 | 0 | 0 | 0 |
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
