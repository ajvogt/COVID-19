# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 07/26/2020  
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
| St. Louis-Farmington | 1174 | 24643 | 656 | 537 | 382 |
| Kansas City | 327 | 18700 | 501 | 419 | 335 |
| Missouri non-MSA | 77 | 6319 | 170 | 154 | 118 |
| Springfield | 12 | 1281 | 59 | 49 | 31 |
| Joplin | 25 | 2217 | 50 | 48 | 50 |
| Columbia-Jefferson City | 8 | 1390 | 41 | 39 | 30 |
| Cape Girardeau-Sikeston | 16 | 890 | 21 | 22 | 19 |
| St. Joseph | 12 | 1158 | 10 | 8 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 628 | 10687 | 260 | 209 | 153 |
| Kansas City | Missouri | Kansas City | 45 | 4718 | 164 | 116 | 85 |
| St. Louis-Farmington | Missouri | St. Charles | 79 | 2547 | 124 | 88 | 51 |
| Kansas City | Kansas | Johnson | 94 | 4387 | 102 | 109 | 98 |
| Kansas City | Missouri | Jackson | 53 | 2433 | 89 | 62 | 45 |
| St. Louis-Farmington | Missouri | St. Louis City | 164 | 3895 | 79 | 69 | 56 |
| Kansas City | Kansas | Wyandotte | 91 | 4056 | 77 | 79 | 68 |
| St. Louis-Farmington | Illinois | St. Clair | 153 | 3106 | 65 | 60 | 47 |
| St. Louis-Farmington | Illinois | Madison | 71 | 1762 | 43 | 42 | 29 |
| Joplin | Missouri | Jasper | 22 | 1487 | 37 | 35 | 36 |
| St. Louis-Farmington | Missouri | Jefferson | 23 | 929 | 34 | 26 | 16 |
| Springfield | Missouri | Greene | 9 | 830 | 33 | 28 | 19 |
| Kansas City | Missouri | Cass | 8 | 429 | 25 | 16 | 10 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 893 | 22 | 23 | 19 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 443 | 13 | 12 | 8 |
| Springfield | Missouri | Polk | 0 | 150 | 13 | 9 | 4 |
| Joplin | Missouri | Newton | 3 | 730 | 13 | 12 | 13 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 3 | 520 | 13 | 13 | 13 |
| Kansas City | Missouri | Clay | 19 | 705 | 12 | 10 | 10 |
| Missouri non-MSA | Missouri | Camden | 3 | 187 | 12 | 7 | 4 |
| Kansas City | Kansas | Leavenworth | 7 | 1337 | 12 | 8 | 6 |
| Missouri non-MSA | Missouri | McDonald | 7 | 881 | 11 | 12 | 14 |
| Missouri non-MSA | Missouri | Taney | 3 | 237 | 10 | 8 | 6 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 212 | 9 | 7 | 3 |
| Missouri non-MSA | Missouri | Johnson | 1 | 416 | 9 | 12 | 10 |
| Missouri non-MSA | Missouri | Pettis | 3 | 259 | 9 | 8 | 4 |
| Springfield | Missouri | Christian | 1 | 168 | 7 | 6 | 4 |
| Columbia-Jefferson City | Missouri | Cole | 2 | 211 | 7 | 7 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 3 | 194 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 134 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Butler | 2 | 189 | 6 | 5 | 3 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 286 | 6 | 5 | 4 |
| St. Joseph | Missouri | Buchanan | 10 | 1015 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 72 | 6 | 3 | 1 |
| St. Louis-Farmington | Missouri | Warren | 0 | 117 | 5 | 4 | 2 |
| Kansas City | Missouri | Platte | 6 | 236 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Marion | 1 | 82 | 5 | 3 | 2 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 225 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Laclede | 1 | 170 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Howell | 0 | 98 | 5 | 3 | 2 |
| Missouri non-MSA | Missouri | Barry | 0 | 187 | 4 | 6 | 5 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 220 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 127 | 4 | 5 | 3 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 294 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Audrain | 1 | 181 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Saline | 6 | 368 | 3 | 4 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 37 | 3 | 2 | 1 |
| Kansas City | Kansas | Miami | 0 | 92 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Carroll | 0 | 69 | 3 | 3 | 1 |
| Missouri non-MSA | Missouri | Stone | 1 | 58 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Douglas | 1 | 43 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 121 | 3 | 1 | 1 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 106 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Pemiscot | 6 | 179 | 2 | 4 | 2 |
| Springfield | Missouri | Webster | 1 | 93 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Benton | 0 | 51 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Miller | 0 | 60 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 188 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 87 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 170 | 2 | 2 | 1 |
| Kansas City | Missouri | Clinton | 0 | 53 | 2 | 1 | 1 |
| Springfield | Missouri | Dallas | 1 | 40 | 1 | 1 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 73 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Morgan | 0 | 42 | 1 | 1 | 0 |
| St. Louis-Farmington | Illinois | Bond | 1 | 36 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 36 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 90 | 1 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 43 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 0 | 29 | 1 | 1 | 0 |
| Kansas City | Missouri | Bates | 1 | 29 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Adair | 0 | 118 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 0 | 40 | 1 | 0 | 1 |
| Missouri non-MSA | Missouri | Lewis | 1 | 20 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 37 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 43 | 1 | 1 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 49 | 1 | 2 | 1 |
| Kansas City | Missouri | Ray | 0 | 47 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Perry | 3 | 187 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Henry | 3 | 49 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 44 | 1 | 1 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 125 | 1 | 1 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 59 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Pike | 1 | 54 | 1 | 1 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 27 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 52 | 1 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 1 | 27 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 12 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Washington | 1 | 46 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 13 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 28 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 37 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 15 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Phelps | 0 | 59 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 31 | 0 | 1 | 0 |
| Kansas City | Kansas | Linn | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Randolph | 1 | 26 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Texas | 0 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Crawford | 0 | 33 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 27 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 44 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 17 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 73 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 124 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 38 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 2 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 53 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 2 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 10 | 0 | 0 | 0 |
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
