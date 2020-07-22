# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 07/22/2020  
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
| St. Louis-Farmington | 1151 | 21384 | 465 | 416 | 287 |
| Kansas City | 311 | 16350 | 393 | 350 | 281 |
| Missouri non-MSA | 65 | 5469 | 145 | 122 | 99 |
| Springfield | 12 | 1019 | 50 | 36 | 24 |
| Joplin | 23 | 1968 | 46 | 45 | 47 |
| Columbia-Jefferson City | 7 | 1163 | 34 | 31 | 24 |
| Cape Girardeau-Sikeston | 16 | 801 | 24 | 23 | 16 |
| St. Joseph | 11 | 1116 | 8 | 7 | 7 |
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
| St. Louis-Farmington | Missouri | St. Louis | 610 | 9361 | 174 | 163 | 117 |
| Kansas City | Kansas | Johnson | 95 | 3886 | 104 | 109 | 87 |
| Kansas City | Missouri | Kansas City | 41 | 3924 | 101 | 79 | 66 |
| Kansas City | Kansas | Wyandotte | 89 | 3749 | 90 | 79 | 63 |
| St. Louis-Farmington | Missouri | St. Louis City | 161 | 3518 | 67 | 61 | 39 |
| St. Louis-Farmington | Missouri | St. Charles | 79 | 1909 | 67 | 53 | 31 |
| St. Louis-Farmington | Illinois | St. Clair | 151 | 2794 | 58 | 52 | 39 |
| Kansas City | Missouri | Jackson | 48 | 1988 | 48 | 42 | 32 |
| St. Louis-Farmington | Illinois | Madison | 71 | 1540 | 36 | 34 | 24 |
| Joplin | Missouri | Jasper | 20 | 1290 | 33 | 32 | 34 |
| Springfield | Missouri | Greene | 9 | 668 | 25 | 21 | 14 |
| St. Louis-Farmington | Missouri | Jefferson | 23 | 763 | 21 | 17 | 12 |
| Columbia-Jefferson City | Missouri | Boone | 2 | 758 | 18 | 21 | 16 |
| Missouri non-MSA | Missouri | Johnson | 1 | 381 | 16 | 13 | 9 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 3 | 473 | 16 | 15 | 11 |
| Kansas City | Missouri | Cass | 8 | 314 | 13 | 10 | 6 |
| Springfield | Missouri | Polk | 0 | 114 | 13 | 7 | 3 |
| Joplin | Missouri | Newton | 3 | 678 | 13 | 12 | 13 |
| Missouri non-MSA | Missouri | McDonald | 1 | 822 | 11 | 12 | 15 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 382 | 11 | 10 | 6 |
| Kansas City | Missouri | Clay | 13 | 646 | 9 | 9 | 10 |
| Missouri non-MSA | Missouri | Barry | 0 | 172 | 9 | 6 | 4 |
| Kansas City | Kansas | Leavenworth | 7 | 1285 | 8 | 6 | 5 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 109 | 7 | 4 | 2 |
| Columbia-Jefferson City | Missouri | Cole | 2 | 167 | 7 | 5 | 3 |
| Kansas City | Missouri | Platte | 6 | 213 | 7 | 5 | 3 |
| Missouri non-MSA | Missouri | Taney | 3 | 184 | 7 | 5 | 5 |
| Missouri non-MSA | Missouri | Laclede | 1 | 148 | 6 | 6 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 106 | 6 | 4 | 3 |
| Springfield | Missouri | Christian | 1 | 126 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Pettis | 2 | 204 | 5 | 4 | 3 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 160 | 5 | 3 | 2 |
| St. Louis-Farmington | Missouri | Warren | 0 | 97 | 5 | 3 | 2 |
| St. Joseph | Missouri | Buchanan | 9 | 991 | 5 | 5 | 6 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 207 | 4 | 3 | 4 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 250 | 4 | 4 | 3 |
| Missouri non-MSA | Missouri | Saline | 6 | 349 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 6 | 165 | 4 | 3 | 2 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 199 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Butler | 0 | 151 | 4 | 2 | 2 |
| Springfield | Missouri | Webster | 1 | 80 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Camden | 2 | 114 | 3 | 2 | 2 |
| Missouri non-MSA | Missouri | Dunklin | 3 | 160 | 3 | 3 | 2 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 95 | 3 | 2 | 1 |
| Kansas City | Kansas | Miami | 0 | 79 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 176 | 3 | 2 | 1 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 273 | 3 | 2 | 1 |
| Missouri non-MSA | Missouri | Audrain | 1 | 163 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 45 | 2 | 1 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 24 | 2 | 1 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 46 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Marion | 0 | 53 | 2 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 81 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Cedar | 0 | 29 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Miller | 0 | 44 | 2 | 1 | 1 |
| Kansas City | Missouri | Lafayette | 2 | 120 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 42 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Douglas | 1 | 31 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Washington | 1 | 41 | 2 | 1 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 51 | 2 | 1 | 1 |
| St. Joseph | Missouri | Andrew | 1 | 68 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Howell | 0 | 65 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 0 | 28 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Adair | 0 | 114 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 157 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Perry | 3 | 183 | 1 | 1 | 2 |
| Springfield | Missouri | Dallas | 1 | 31 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Stone | 0 | 41 | 1 | 1 | 1 |
| St. Joseph | Kansas | Doniphan | 0 | 36 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Ripley | 0 | 30 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carroll | 0 | 49 | 1 | 2 | 1 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 54 | 1 | 1 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 24 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 36 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 125 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Phelps | 0 | 59 | 1 | 0 | 1 |
| Kansas City | Missouri | Ray | 0 | 38 | 1 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 32 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Benton | 0 | 33 | 1 | 0 | 0 |
| Kansas City | Missouri | Clinton | 0 | 42 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Crawford | 0 | 30 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Pike | 1 | 50 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Bond | 1 | 28 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 0 | 51 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Harrison | 1 | 37 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Shannon | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Morgan | 0 | 34 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 104 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 41 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 30 | 0 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 14 | 0 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 20 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 34 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 21 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 14 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 70 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Lewis | 1 | 12 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 71 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Texas | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Livingston | 0 | 30 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 7 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Monroe | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 24 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 11 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Worth | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 0 | 3 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 3 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 4 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 2 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 2 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 1 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 11 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 0 | 2 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 22 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Randolph | 1 | 21 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Wayne | 0 | 5 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 14 | 0 | 0 | 0 |
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
