# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 02/22/2021  
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
County populations are pulled from this 
[JHU CSSE repository file](https://github.com/ajvogt/COVID-19/blob/master/csse_covid_19_data/UID_ISO_FIPS_LookUp_Table.csv).

## Missouri New Daily Confirmed Cases by Metropolitan Statistcal Areas
![](images/mo_daily_cases.png)

## Missouri New Daily Deaths by Metropolitan Statistcal Areas
![](images/mo_daily_deaths.png)

## Missouri Cumulative Deaths by Metropolitan Statistcal Areas
![](images/mo_cumulative_deaths.png)

## Missouri Metropolitan Statistical Area Totals
<!-- msa_table start -->
| MSA | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|
| Kansas City | 2427 | 174339 | 451 | 399 | 498 |
| St. Louis-Farmington | 4472 | 253981 | 376 | 453 | 646 |
| Missouri non-MSA | 1965 | 109322 | 99 | 112 | 184 |
| Springfield | 592 | 35988 | 35 | 47 | 74 |
| Columbia-Jefferson City | 304 | 34297 | 30 | 32 | 57 |
| Joplin | 278 | 16185 | 16 | 21 | 36 |
| Cape Girardeau-Sikeston | 207 | 12773 | 13 | 13 | 21 |
| St. Joseph | 192 | 10055 | 8 | 8 | 15 |
<!-- msa_table end -->

## STL-Farmington MSA New Daily Confirmed Cases by County
![](images/stl_daily_cases.png)

## STL-Farmington MSA New Daily Deaths by County
![](images/stl_daily_deaths.png)

## STL-Farmington MSA Cumulative Deaths by County
![](images/stl_cumulative_deaths.png)

<a name="msa-counties"></a>
## Metropolitan Statistical Area (MSA) Counties
<!-- county_table start -->
| MSA | State | County | Total Deaths | Total Cases | Daily New Cases: Last 7-Day Average | Daily New Cases: Last 14-Day Average | Daily New Cases: Last 30-Day Average |
|-----|-------|--------|---|---|---|---|---|
| Kansas City | Kansas | Johnson | 733 | 53652 | 254 | 195 | 191 |
| St. Louis-Farmington | Missouri | St. Louis | 1917 | 87465 | 139 | 164 | 239 |
| Kansas City | Missouri | Jackson | 370 | 29875 | 56 | 60 | 90 |
| St. Louis-Farmington | Illinois | Madison | 449 | 27664 | 46 | 58 | 88 |
| St. Louis-Farmington | Illinois | St. Clair | 463 | 25097 | 46 | 54 | 77 |
| Kansas City | Kansas | Wyandotte | 264 | 18935 | 40 | 37 | 39 |
| St. Louis-Farmington | Missouri | St. Charles | 405 | 32702 | 37 | 54 | 63 |
| Kansas City | Missouri | Kansas City | 496 | 36552 | 36 | 36 | 77 |
| St. Louis-Farmington | Missouri | St. Louis City | 412 | 21208 | 33 | 36 | 45 |
| Springfield | Missouri | Greene | 416 | 23220 | 25 | 33 | 50 |
| St. Louis-Farmington | Missouri | Jefferson | 204 | 18872 | 20 | 22 | 40 |
| Kansas City | Kansas | Leavenworth | 76 | 6680 | 17 | 21 | 23 |
| Columbia-Jefferson City | Missouri | Boone | 77 | 15824 | 16 | 17 | 30 |
| Joplin | Missouri | Jasper | 214 | 12126 | 13 | 16 | 28 |
| St. Louis-Farmington | Missouri | Franklin | 153 | 8358 | 12 | 13 | 18 |
| Kansas City | Missouri | Clay | 143 | 7816 | 12 | 11 | 19 |
| Missouri non-MSA | Missouri | Butler | 33 | 3422 | 9 | 9 | 9 |
| Kansas City | Missouri | Cass | 84 | 7165 | 9 | 12 | 20 |
| St. Louis-Farmington | Missouri | Lincoln | 32 | 4267 | 7 | 8 | 10 |
| St. Louis-Farmington | Missouri | St. Francois | 102 | 7550 | 6 | 6 | 10 |
| St. Louis-Farmington | Illinois | Monroe | 80 | 4025 | 6 | 7 | 12 |
| Columbia-Jefferson City | Missouri | Callaway | 43 | 4454 | 6 | 5 | 9 |
| Springfield | Missouri | Christian | 75 | 6822 | 6 | 7 | 14 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 114 | 7485 | 6 | 7 | 13 |
| Kansas City | Missouri | Ray | 23 | 1500 | 6 | 4 | 5 |
| Cape Girardeau-Sikeston | Missouri | Scott | 73 | 3795 | 5 | 5 | 6 |
| Kansas City | Kansas | Miami | 39 | 2592 | 5 | 5 | 6 |
| St. Joseph | Missouri | Buchanan | 129 | 6929 | 5 | 5 | 10 |
| Missouri non-MSA | Missouri | Johnson | 43 | 3842 | 5 | 6 | 8 |
| St. Louis-Farmington | Illinois | Macoupin | 78 | 4314 | 5 | 7 | 11 |
| Columbia-Jefferson City | Missouri | Cole | 114 | 8551 | 5 | 6 | 11 |
| Missouri non-MSA | Missouri | Taney | 82 | 4551 | 4 | 5 | 8 |
| Kansas City | Missouri | Platte | 42 | 3069 | 4 | 4 | 8 |
| Missouri non-MSA | Missouri | Phelps | 121 | 2983 | 4 | 3 | 5 |
| Kansas City | Missouri | Lafayette | 53 | 2532 | 3 | 4 | 6 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1888 | 3 | 4 | 3 |
| St. Louis-Farmington | Illinois | Jersey | 45 | 2473 | 3 | 4 | 6 |
| Joplin | Missouri | Newton | 64 | 4059 | 3 | 5 | 7 |
| St. Louis-Farmington | Illinois | Clinton | 89 | 5544 | 3 | 6 | 13 |
| Missouri non-MSA | Missouri | Nodaway | 24 | 2555 | 3 | 2 | 2 |
| St. Louis-Farmington | Missouri | Warren | 17 | 2081 | 3 | 3 | 5 |
| Missouri non-MSA | Missouri | Barry | 44 | 2177 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Stone | 36 | 2014 | 2 | 2 | 5 |
| Missouri non-MSA | Missouri | Laclede | 64 | 2916 | 2 | 1 | 5 |
| Missouri non-MSA | Missouri | Perry | 24 | 2038 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Pettis | 75 | 4755 | 2 | 4 | 7 |
| Missouri non-MSA | Missouri | Henry | 36 | 1729 | 2 | 3 | 4 |
| Missouri non-MSA | Missouri | Pulaski | 43 | 2974 | 2 | 2 | 3 |
| Missouri non-MSA | Missouri | Saline | 35 | 2415 | 2 | 2 | 4 |
| Missouri non-MSA | Missouri | Vernon | 39 | 1383 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 14 | 1613 | 2 | 1 | 2 |
| Missouri non-MSA | Missouri | Lawrence | 71 | 2742 | 1 | 3 | 5 |
| Missouri non-MSA | Missouri | Benton | 25 | 1444 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Washington | 45 | 2117 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Howell | 42 | 2791 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Marion | 41 | 2640 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Stoddard | 36 | 2295 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Barton | 12 | 955 | 1 | 1 | 2 |
| Springfield | Missouri | Polk | 30 | 2141 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Camden | 80 | 3699 | 1 | 2 | 5 |
| Missouri non-MSA | Missouri | Livingston | 36 | 1324 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Crawford | 29 | 2039 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Grundy | 34 | 828 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 24 | 1255 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Clark | 6 | 470 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Texas | 22 | 1535 | 1 | 1 | 1 |
| Kansas City | Missouri | Clinton | 64 | 1519 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Miller | 49 | 2313 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | McDonald | 25 | 1911 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Dunklin | 17 | 2403 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Adair | 16 | 2054 | 1 | 2 | 4 |
| Missouri non-MSA | Missouri | Audrain | 57 | 2066 | 1 | 1 | 3 |
| Columbia-Jefferson City | Missouri | Osage | 12 | 1394 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Ripley | 14 | 851 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Macon | 13 | 1200 | 1 | 1 | 3 |
| Kansas City | Kansas | Linn | 8 | 743 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Gasconade | 38 | 873 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Pike | 21 | 1483 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 28 | 1408 | 1 | 0 | 1 |
| Springfield | Missouri | Webster | 49 | 2987 | 1 | 1 | 4 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 8 | 442 | 1 | 1 | 1 |
| St. Joseph | Missouri | DeKalb | 26 | 917 | 1 | 0 | 1 |
| St. Joseph | Missouri | Andrew | 17 | 1280 | 1 | 1 | 1 |
| Kansas City | Missouri | Bates | 22 | 1070 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Carroll | 22 | 832 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Chariton | 6 | 418 | 1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Cooper | 24 | 1684 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Monroe | 10 | 591 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 20 | 929 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Dent | 16 | 816 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 567 | 0 | 0 | 0 |
| Kansas City | Missouri | Caldwell | 10 | 639 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 257 | 0 | 1 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 473 | 0 | 0 | 0 |
| Springfield | Missouri | Dallas | 22 | 818 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Daviess | 11 | 586 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Wright | 27 | 1365 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Morgan | 39 | 1620 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Lewis | 5 | 628 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ozark | 12 | 547 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dade | 13 | 418 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Harrison | 14 | 826 | 0 | 0 | 2 |
| Missouri non-MSA | Missouri | Cedar | 17 | 666 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 10 | 479 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 12 | 755 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Randolph | 28 | 1806 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | New Madrid | 45 | 1768 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Maries | 7 | 533 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Iron | 5 | 465 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Oregon | 3 | 672 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 366 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 13 | 746 | 0 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 29 | 1678 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Worth | 1 | 141 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1051 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | St. Clair | 7 | 576 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Mercer | 2 | 177 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Gentry | 20 | 734 | 0 | 0 | 1 |
| Columbia-Jefferson City | Missouri | Howard | 5 | 712 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 23 | 765 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Knox | 2 | 176 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Linn | 11 | 540 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Wayne | 10 | 813 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Hickory | 13 | 466 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 290 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 2 | 223 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 260 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 3 | 263 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Shelby | 6 | 349 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Madison | 16 | 1342 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Carter | 8 | 417 | 0 | 0 | 0 |
<!-- county_table end -->

<a name="release-notes"></a>
## Release Notes

### Release Notes
* 1/17/2021: including cumulative deaths plots
* 1/4/2021: small fix for including 2021 data
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

### To-Do (updated 1/17/2021)
- [ ] Verify county population data

#### Analysis Page
- [x] Update description to accurately reflect CSA vs. MSA
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
