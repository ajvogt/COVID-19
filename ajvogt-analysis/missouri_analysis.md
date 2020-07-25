# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 07/25/2020  
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
| St. Louis-Farmington | 1172 | 23777 | 602 | 502 | 362 |
| Kansas City | 328 | 18187 | 484 | 403 | 325 |
| Missouri non-MSA | 76 | 6143 | 173 | 148 | 115 |
| Springfield | 12 | 1215 | 60 | 45 | 29 |
| Joplin | 24 | 2157 | 48 | 45 | 50 |
| Columbia-Jefferson City | 8 | 1342 | 41 | 38 | 29 |
| Cape Girardeau-Sikeston | 16 | 877 | 24 | 23 | 18 |
| St. Joseph | 12 | 1149 | 11 | 8 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 627 | 10319 | 225 | 195 | 143 |
| Kansas City | Missouri | Kansas City | 43 | 4558 | 157 | 108 | 83 |
| St. Louis-Farmington | Missouri | St. Charles | 79 | 2390 | 115 | 80 | 47 |
| Kansas City | Kansas | Johnson | 97 | 4280 | 102 | 111 | 97 |
| Kansas City | Missouri | Jackson | 53 | 2332 | 83 | 56 | 41 |
| St. Louis-Farmington | Missouri | St. Louis City | 164 | 3806 | 78 | 65 | 55 |
| Kansas City | Kansas | Wyandotte | 91 | 3974 | 77 | 78 | 66 |
| St. Louis-Farmington | Illinois | St. Clair | 152 | 3031 | 66 | 59 | 45 |
| St. Louis-Farmington | Illinois | Madison | 71 | 1694 | 40 | 40 | 28 |
| Joplin | Missouri | Jasper | 21 | 1434 | 36 | 33 | 36 |
| Springfield | Missouri | Greene | 9 | 784 | 29 | 25 | 18 |
| St. Louis-Farmington | Missouri | Jefferson | 23 | 876 | 29 | 22 | 14 |
| Kansas City | Missouri | Cass | 8 | 397 | 22 | 14 | 9 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 860 | 22 | 23 | 19 |
| Springfield | Missouri | Polk | 0 | 144 | 16 | 8 | 4 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 3 | 512 | 15 | 14 | 12 |
| Missouri non-MSA | Missouri | McDonald | 7 | 878 | 13 | 13 | 15 |
| Missouri non-MSA | Missouri | Johnson | 1 | 411 | 12 | 13 | 10 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 424 | 12 | 11 | 7 |
| Kansas City | Kansas | Leavenworth | 7 | 1337 | 12 | 8 | 6 |
| Joplin | Missouri | Newton | 3 | 723 | 12 | 12 | 14 |
| Kansas City | Missouri | Clay | 19 | 688 | 11 | 9 | 10 |
| Missouri non-MSA | Missouri | Camden | 3 | 166 | 10 | 6 | 3 |
| Missouri non-MSA | Missouri | Taney | 3 | 226 | 10 | 7 | 6 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 202 | 9 | 6 | 3 |
| Columbia-Jefferson City | Missouri | Cole | 2 | 206 | 9 | 7 | 4 |
| Missouri non-MSA | Missouri | Pettis | 3 | 250 | 9 | 7 | 4 |
| Springfield | Missouri | Christian | 1 | 159 | 7 | 6 | 4 |
| St. Joseph | Missouri | Buchanan | 10 | 1009 | 6 | 5 | 6 |
| Missouri non-MSA | Missouri | Dunklin | 3 | 192 | 6 | 4 | 3 |
| Missouri non-MSA | Missouri | Butler | 1 | 177 | 6 | 4 | 3 |
| St. Louis-Farmington | Missouri | Warren | 0 | 114 | 6 | 4 | 2 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 282 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Laclede | 1 | 168 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 125 | 5 | 5 | 3 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 69 | 5 | 3 | 1 |
| Kansas City | Missouri | Platte | 6 | 230 | 5 | 5 | 4 |
| Missouri non-MSA | Missouri | Saline | 6 | 365 | 5 | 4 | 2 |
| Missouri non-MSA | Missouri | Barry | 0 | 182 | 5 | 6 | 5 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 219 | 5 | 4 | 4 |
| Missouri non-MSA | Missouri | Marion | 1 | 75 | 4 | 3 | 2 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 292 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 124 | 4 | 5 | 2 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 213 | 3 | 4 | 3 |
| Missouri non-MSA | Missouri | Audrain | 1 | 178 | 3 | 2 | 1 |
| Springfield | Missouri | Webster | 1 | 92 | 3 | 3 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 34 | 3 | 2 | 0 |
| Missouri non-MSA | Missouri | Benton | 0 | 52 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Pemiscot | 6 | 176 | 3 | 4 | 2 |
| Kansas City | Kansas | Miami | 0 | 92 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 121 | 3 | 1 | 1 |
| Missouri non-MSA | Missouri | Stone | 1 | 58 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 186 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Miller | 0 | 56 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 167 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Howell | 0 | 78 | 2 | 2 | 1 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 101 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Carroll | 0 | 61 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Douglas | 1 | 40 | 2 | 2 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 124 | 2 | 1 | 1 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 49 | 2 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 0 | 31 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Morgan | 0 | 41 | 1 | 1 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 72 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 36 | 1 | 1 | 0 |
| Springfield | Missouri | Dallas | 1 | 36 | 1 | 1 | 0 |
| Kansas City | Missouri | Clinton | 0 | 50 | 1 | 1 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 43 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Henry | 3 | 46 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 89 | 1 | 1 | 1 |
| Kansas City | Missouri | Bates | 1 | 28 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 53 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Shannon | 0 | 40 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 117 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 44 | 1 | 1 | 1 |
| Kansas City | Missouri | Caldwell | 1 | 27 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 42 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 29 | 1 | 1 | 0 |
| St. Louis-Farmington | Illinois | Bond | 1 | 33 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 35 | 1 | 0 | 0 |
| Kansas City | Missouri | Ray | 0 | 45 | 1 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 80 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Perry | 3 | 186 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Pike | 1 | 54 | 1 | 1 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 58 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 15 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 10 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Phelps | 0 | 59 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Ralls | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 44 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Livingston | 0 | 34 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 27 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 34 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Crawford | 0 | 32 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 8 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Randolph | 1 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 73 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Texas | 0 | 20 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 26 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Washington | 1 | 42 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 52 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 9 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 124 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 37 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 13 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 2 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 2 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 9 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 10 | 0 | 0 | 0 |
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
