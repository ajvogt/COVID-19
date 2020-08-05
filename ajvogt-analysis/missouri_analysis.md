# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 08/05/2020  
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
| St. Louis-Farmington | 1219 | 31969 | 744 | 756 | 560 |
| Kansas City | 359 | 23565 | 477 | 515 | 418 |
| Missouri non-MSA | 94 | 8469 | 218 | 214 | 164 |
| Springfield | 13 | 1970 | 67 | 67 | 50 |
| Columbia-Jefferson City | 10 | 2053 | 64 | 63 | 46 |
| Joplin | 33 | 2503 | 22 | 38 | 42 |
| Cape Girardeau-Sikeston | 17 | 1063 | 14 | 18 | 21 |
| St. Joseph | 12 | 1229 | 7 | 8 | 8 |
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
| St. Louis-Farmington | Missouri | St. Louis | 651 | 13788 | 313 | 316 | 230 |
| Kansas City | Missouri | Kansas City | 55 | 6137 | 124 | 158 | 114 |
| Kansas City | Missouri | Jackson | 59 | 3639 | 120 | 117 | 77 |
| St. Louis-Farmington | Missouri | St. Charles | 87 | 3749 | 119 | 131 | 87 |
| Kansas City | Kansas | Johnson | 98 | 5240 | 93 | 96 | 101 |
| St. Louis-Farmington | Missouri | St. Louis City | 171 | 4740 | 87 | 87 | 71 |
| St. Louis-Farmington | Illinois | St. Clair | 156 | 3696 | 61 | 64 | 55 |
| Kansas City | Kansas | Wyandotte | 96 | 4618 | 60 | 62 | 68 |
| St. Louis-Farmington | Missouri | Jefferson | 24 | 1428 | 51 | 47 | 30 |
| Springfield | Missouri | Greene | 10 | 1301 | 47 | 45 | 32 |
| St. Louis-Farmington | Illinois | Madison | 73 | 2266 | 46 | 51 | 41 |
| Columbia-Jefferson City | Missouri | Boone | 3 | 1259 | 33 | 35 | 28 |
| Missouri non-MSA | Missouri | Taney | 3 | 480 | 28 | 21 | 13 |
| Kansas City | Missouri | Clay | 20 | 944 | 22 | 21 | 14 |
| Kansas City | Missouri | Cass | 9 | 673 | 22 | 25 | 17 |
| Missouri non-MSA | Missouri | Pettis | 3 | 450 | 18 | 17 | 10 |
| Joplin | Missouri | Jasper | 27 | 1675 | 14 | 27 | 30 |
| Columbia-Jefferson City | Missouri | Cole | 3 | 338 | 12 | 12 | 8 |
| Springfield | Missouri | Christian | 1 | 300 | 12 | 12 | 8 |
| St. Louis-Farmington | Missouri | Lincoln | 1 | 331 | 12 | 12 | 7 |
| St. Louis-Farmington | Missouri | Franklin | 18 | 554 | 12 | 12 | 11 |
| Missouri non-MSA | Missouri | Camden | 5 | 317 | 10 | 14 | 8 |
| St. Louis-Farmington | Missouri | St. Francois | 2 | 320 | 10 | 8 | 5 |
| Kansas City | Kansas | Leavenworth | 8 | 1425 | 9 | 10 | 8 |
| Missouri non-MSA | Missouri | Marion | 1 | 160 | 8 | 7 | 4 |
| Missouri non-MSA | Missouri | New Madrid | 1 | 200 | 8 | 6 | 5 |
| Kansas City | Missouri | Platte | 10 | 328 | 8 | 8 | 6 |
| Joplin | Missouri | Newton | 6 | 828 | 8 | 10 | 12 |
| Missouri non-MSA | Missouri | Nodaway | 0 | 165 | 8 | 8 | 4 |
| St. Louis-Farmington | Illinois | Monroe | 13 | 284 | 7 | 6 | 5 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 4 | 613 | 7 | 10 | 13 |
| St. Louis-Farmington | Missouri | Warren | 0 | 180 | 7 | 5 | 4 |
| Missouri non-MSA | Missouri | Dunklin | 4 | 267 | 7 | 7 | 5 |
| Missouri non-MSA | Missouri | Johnson | 2 | 473 | 6 | 6 | 10 |
| Cape Girardeau-Sikeston | Missouri | Scott | 13 | 356 | 6 | 7 | 5 |
| Missouri non-MSA | Missouri | McDonald | 7 | 940 | 6 | 8 | 10 |
| Missouri non-MSA | Missouri | Lawrence | 2 | 195 | 6 | 6 | 5 |
| St. Louis-Farmington | Illinois | Clinton | 17 | 353 | 6 | 5 | 3 |
| Missouri non-MSA | Missouri | Butler | 2 | 249 | 5 | 7 | 4 |
| Missouri non-MSA | Missouri | Saline | 7 | 416 | 5 | 4 | 4 |
| Columbia-Jefferson City | Missouri | Cooper | 0 | 103 | 5 | 4 | 2 |
| Kansas City | Missouri | Ray | 0 | 103 | 5 | 4 | 2 |
| St. Joseph | Missouri | Buchanan | 10 | 1063 | 5 | 5 | 5 |
| Columbia-Jefferson City | Missouri | Moniteau | 2 | 130 | 4 | 4 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 8 | 220 | 4 | 3 | 3 |
| Columbia-Jefferson City | Missouri | Callaway | 1 | 131 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Howell | 2 | 142 | 4 | 5 | 3 |
| Missouri non-MSA | Missouri | Douglas | 2 | 83 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Miller | 0 | 107 | 4 | 4 | 2 |
| Kansas City | Missouri | Lafayette | 2 | 164 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Wayne | 0 | 44 | 4 | 2 | 1 |
| Missouri non-MSA | Missouri | Barry | 2 | 233 | 3 | 4 | 5 |
| Missouri non-MSA | Missouri | Crawford | 0 | 58 | 3 | 2 | 1 |
| St. Louis-Farmington | Illinois | Macoupin | 3 | 142 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Stone | 1 | 95 | 3 | 3 | 2 |
| Springfield | Missouri | Polk | 0 | 194 | 3 | 5 | 5 |
| Missouri non-MSA | Missouri | Laclede | 1 | 199 | 3 | 3 | 5 |
| Springfield | Missouri | Webster | 1 | 123 | 3 | 3 | 2 |
| Missouri non-MSA | Missouri | Carroll | 0 | 99 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Texas | 0 | 43 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Perry | 4 | 211 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Shelby | 0 | 30 | 2 | 1 | 0 |
| Kansas City | Kansas | Miami | 0 | 120 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Harrison | 1 | 60 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 0 | 71 | 2 | 2 | 1 |
| St. Louis-Farmington | Illinois | Bond | 2 | 57 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Henry | 3 | 73 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Pike | 1 | 78 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Knox | 0 | 19 | 2 | 1 | 0 |
| St. Louis-Farmington | Illinois | Jersey | 1 | 73 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Adair | 0 | 137 | 2 | 1 | 1 |
| Missouri non-MSA | Missouri | Audrain | 1 | 194 | 2 | 2 | 1 |
| Missouri non-MSA | Missouri | Benton | 1 | 75 | 2 | 3 | 1 |
| Missouri non-MSA | Missouri | Livingston | 0 | 53 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pulaski | 1 | 187 | 1 | 2 | 1 |
| Columbia-Jefferson City | Missouri | Osage | 1 | 45 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Clark | 0 | 14 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Phelps | 0 | 76 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 0 | 22 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Washington | 1 | 60 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 1 | 21 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 0 | 20 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Macon | 0 | 54 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Randolph | 1 | 57 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Stoddard | 9 | 212 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Dade | 0 | 21 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 0 | 40 | 1 | 1 | 0 |
| Springfield | Missouri | Dallas | 1 | 52 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Ripley | 1 | 46 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Ralls | 0 | 25 | 1 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 1 | 12 | 1 | 0 | 0 |
| Kansas City | Kansas | Linn | 0 | 35 | 1 | 0 | 0 |
| Kansas City | Missouri | Bates | 1 | 40 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 0 | 137 | 1 | 0 | 0 |
| Kansas City | Missouri | Clinton | 0 | 65 | 1 | 1 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 0 | 47 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Lewis | 1 | 34 | 1 | 1 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 0 | 21 | 1 | 0 | 0 |
| St. Joseph | Missouri | Andrew | 1 | 85 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Maries | 0 | 17 | 0 | 0 | 0 |
| St. Joseph | Missouri | DeKalb | 1 | 35 | 0 | 1 | 0 |
| Kansas City | Missouri | Caldwell | 1 | 34 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 0 | 58 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 0 | 131 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 1 | 48 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 0 | 19 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Barton | 0 | 66 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Wright | 0 | 58 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Cedar | 0 | 35 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 0 | 17 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Chariton | 0 | 17 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 0 | 46 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 0 | 16 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 9 | 82 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 1 | 30 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shannon | 1 | 43 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 0 | 10 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 0 | 14 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 0 | 8 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Vernon | 0 | 47 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 0 | 36 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 1 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 0 | 6 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Grundy | 1 | 25 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 0 | 12 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dent | 0 | 9 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Daviess | 0 | 17 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 0 | 17 | 0 | 0 | 0 |
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
