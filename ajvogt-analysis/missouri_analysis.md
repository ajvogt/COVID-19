# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 01/21/2021  
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
| St. Louis-Farmington | 3881 | 229911 | 1155 | 1425 | 1397 |
| Kansas City | 1981 | 157506 | 918 | 1086 | 1069 |
| Missouri non-MSA | 1636 | 102903 | 372 | 522 | 544 |
| Springfield | 488 | 33433 | 138 | 194 | 207 |
| Columbia-Jefferson City | 255 | 32328 | 95 | 132 | 147 |
| Joplin | 242 | 14968 | 50 | 71 | 74 |
| Cape Girardeau-Sikeston | 195 | 12044 | 35 | 46 | 49 |
| St. Joseph | 167 | 9501 | 32 | 42 | 43 |
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
| St. Louis-Farmington | Missouri | St. Louis | 1604 | 79512 | 415 | 543 | 487 |
| Kansas City | Kansas | Johnson | 618 | 47051 | 386 | 406 | 369 |
| St. Louis-Farmington | Illinois | Madison | 468 | 24604 | 164 | 181 | 173 |
| St. Louis-Farmington | Illinois | St. Clair | 429 | 22480 | 151 | 175 | 162 |
| Kansas City | Missouri | Kansas City | 412 | 34009 | 140 | 187 | 191 |
| Kansas City | Missouri | Jackson | 290 | 26934 | 137 | 178 | 172 |
| St. Louis-Farmington | Missouri | St. Charles | 332 | 30515 | 123 | 166 | 168 |
| St. Louis-Farmington | Missouri | Jefferson | 164 | 17476 | 89 | 114 | 113 |
| Springfield | Missouri | Greene | 337 | 21511 | 89 | 125 | 133 |
| Kansas City | Kansas | Wyandotte | 222 | 17568 | 75 | 91 | 109 |
| Columbia-Jefferson City | Missouri | Boone | 58 | 14773 | 52 | 67 | 73 |
| St. Louis-Farmington | Missouri | Franklin | 127 | 7694 | 44 | 54 | 53 |
| Kansas City | Kansas | Leavenworth | 51 | 5866 | 41 | 41 | 36 |
| Joplin | Missouri | Jasper | 182 | 11153 | 41 | 54 | 56 |
| Kansas City | Missouri | Cass | 68 | 6493 | 38 | 49 | 46 |
| Kansas City | Missouri | Clay | 120 | 7147 | 30 | 44 | 45 |
| Springfield | Missouri | Christian | 61 | 6329 | 28 | 39 | 41 |
| St. Louis-Farmington | Illinois | Clinton | 86 | 5082 | 28 | 29 | 30 |
| St. Louis-Farmington | Illinois | Macoupin | 94 | 3879 | 25 | 33 | 28 |
| St. Louis-Farmington | Missouri | St. Louis City | 303 | 17632 | 25 | 16 | 54 |
| Kansas City | Kansas | Miami | 22 | 2343 | 23 | 24 | 25 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 108 | 7044 | 22 | 28 | 31 |
| St. Joseph | Missouri | Buchanan | 117 | 6577 | 21 | 26 | 27 |
| St. Louis-Farmington | Missouri | St. Francois | 81 | 7195 | 20 | 31 | 36 |
| St. Louis-Farmington | Illinois | Monroe | 71 | 3608 | 20 | 23 | 26 |
| Columbia-Jefferson City | Missouri | Cole | 104 | 8176 | 16 | 25 | 30 |
| Missouri non-MSA | Missouri | Taney | 67 | 4247 | 16 | 24 | 22 |
| Missouri non-MSA | Missouri | Phelps | 107 | 2812 | 15 | 15 | 17 |
| St. Louis-Farmington | Illinois | Jersey | 58 | 2242 | 15 | 13 | 15 |
| Missouri non-MSA | Missouri | Butler | 22 | 3118 | 14 | 15 | 14 |
| Springfield | Missouri | Webster | 45 | 2813 | 13 | 18 | 18 |
| St. Louis-Farmington | Missouri | Lincoln | 24 | 3925 | 12 | 18 | 20 |
| Missouri non-MSA | Missouri | Johnson | 34 | 3559 | 12 | 17 | 16 |
| Missouri non-MSA | Missouri | Howell | 41 | 2649 | 12 | 16 | 16 |
| Missouri non-MSA | Missouri | Barry | 40 | 2046 | 12 | 13 | 10 |
| Kansas City | Missouri | Platte | 30 | 2799 | 11 | 18 | 21 |
| Missouri non-MSA | Missouri | Adair | 7 | 1897 | 11 | 14 | 15 |
| Missouri non-MSA | Missouri | Camden | 69 | 3520 | 10 | 18 | 19 |
| Missouri non-MSA | Missouri | Pettis | 68 | 4473 | 10 | 21 | 22 |
| Kansas City | Missouri | Lafayette | 45 | 2313 | 10 | 11 | 13 |
| Missouri non-MSA | Missouri | Washington | 41 | 2005 | 10 | 11 | 10 |
| St. Louis-Farmington | Missouri | Warren | 12 | 1881 | 9 | 11 | 12 |
| Joplin | Missouri | Newton | 60 | 3815 | 9 | 16 | 17 |
| Columbia-Jefferson City | Missouri | Callaway | 32 | 4153 | 9 | 17 | 21 |
| Cape Girardeau-Sikeston | Missouri | Scott | 68 | 3592 | 8 | 12 | 13 |
| Missouri non-MSA | Missouri | Pulaski | 33 | 2866 | 8 | 19 | 19 |
| Missouri non-MSA | Missouri | Laclede | 54 | 2749 | 8 | 11 | 13 |
| Missouri non-MSA | Missouri | Stone | 29 | 1851 | 8 | 10 | 11 |
| Missouri non-MSA | Missouri | Macon | 10 | 1083 | 7 | 8 | 7 |
| Missouri non-MSA | Missouri | Saline | 28 | 2246 | 7 | 11 | 11 |
| Missouri non-MSA | Missouri | Wright | 24 | 1276 | 7 | 9 | 10 |
| Missouri non-MSA | Missouri | Crawford | 23 | 1922 | 7 | 10 | 13 |
| Missouri non-MSA | Missouri | Randolph | 20 | 1774 | 7 | 9 | 8 |
| Missouri non-MSA | Missouri | Dunklin | 16 | 2277 | 7 | 10 | 9 |
| Missouri non-MSA | Missouri | Stoddard | 35 | 2164 | 7 | 7 | 6 |
| Missouri non-MSA | Missouri | Nodaway | 22 | 2492 | 6 | 7 | 7 |
| Kansas City | Missouri | Ray | 15 | 1321 | 6 | 9 | 10 |
| Missouri non-MSA | Missouri | Livingston | 25 | 1200 | 6 | 9 | 8 |
| Columbia-Jefferson City | Missouri | Cooper | 21 | 1612 | 6 | 6 | 6 |
| Missouri non-MSA | Missouri | McDonald | 23 | 1827 | 6 | 8 | 8 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1744 | 6 | 9 | 10 |
| Missouri non-MSA | Missouri | Harrison | 10 | 737 | 6 | 5 | 5 |
| Kansas City | Missouri | Clinton | 60 | 1426 | 5 | 8 | 8 |
| Missouri non-MSA | Missouri | Marion | 34 | 2528 | 5 | 8 | 10 |
| Missouri non-MSA | Missouri | Vernon | 30 | 1286 | 5 | 9 | 12 |
| Missouri non-MSA | Missouri | Ozark | 5 | 487 | 5 | 6 | 4 |
| Missouri non-MSA | Missouri | Henry | 26 | 1586 | 5 | 8 | 7 |
| Missouri non-MSA | Missouri | Miller | 45 | 2225 | 5 | 9 | 10 |
| Missouri non-MSA | Missouri | Gasconade | 32 | 802 | 5 | 6 | 5 |
| Missouri non-MSA | Missouri | Texas | 20 | 1477 | 5 | 5 | 7 |
| Columbia-Jefferson City | Missouri | Osage | 9 | 1314 | 5 | 6 | 6 |
| Missouri non-MSA | Missouri | Pike | 17 | 1400 | 5 | 7 | 7 |
| Missouri non-MSA | Missouri | Audrain | 45 | 1955 | 5 | 8 | 15 |
| Missouri non-MSA | Missouri | Clark | 5 | 425 | 4 | 3 | 2 |
| Missouri non-MSA | Missouri | Wayne | 9 | 762 | 4 | 5 | 4 |
| Missouri non-MSA | Missouri | Benton | 19 | 1350 | 4 | 7 | 7 |
| Kansas City | Kansas | Linn | 5 | 666 | 4 | 6 | 7 |
| Springfield | Missouri | Polk | 25 | 2021 | 4 | 9 | 10 |
| St. Joseph | Kansas | Doniphan | 11 | 849 | 4 | 6 | 5 |
| Missouri non-MSA | Missouri | Dent | 10 | 771 | 4 | 3 | 4 |
| Columbia-Jefferson City | Missouri | Moniteau | 27 | 1623 | 4 | 6 | 6 |
| Missouri non-MSA | Missouri | Grundy | 30 | 779 | 4 | 5 | 5 |
| Missouri non-MSA | Missouri | Cedar | 9 | 615 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Barton | 10 | 883 | 3 | 6 | 5 |
| St. Joseph | Missouri | DeKalb | 23 | 862 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Douglas | 21 | 719 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Morgan | 31 | 1569 | 3 | 6 | 6 |
| Missouri non-MSA | Missouri | Sullivan | 12 | 728 | 3 | 3 | 3 |
| Missouri non-MSA | Missouri | Perry | 22 | 1959 | 3 | 4 | 5 |
| Kansas City | Missouri | Bates | 15 | 971 | 3 | 6 | 7 |
| Missouri non-MSA | Missouri | Carroll | 18 | 740 | 3 | 4 | 4 |
| Missouri non-MSA | Missouri | Lawrence | 62 | 2561 | 3 | 10 | 12 |
| Missouri non-MSA | Missouri | Lewis | 3 | 609 | 3 | 3 | 3 |
| St. Joseph | Missouri | Andrew | 16 | 1213 | 2 | 4 | 6 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 7 | 393 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Gentry | 18 | 684 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Oregon | 3 | 636 | 2 | 5 | 4 |
| St. Louis-Farmington | Illinois | Calhoun | 4 | 442 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Linn | 10 | 486 | 2 | 4 | 3 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 12 | 1521 | 2 | 4 | 6 |
| Springfield | Missouri | Dallas | 20 | 759 | 2 | 3 | 2 |
| Missouri non-MSA | Missouri | Pemiscot | 23 | 1355 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | Ripley | 10 | 749 | 2 | 3 | 3 |
| Missouri non-MSA | Missouri | New Madrid | 40 | 1708 | 2 | 4 | 5 |
| Missouri non-MSA | Missouri | Maries | 7 | 505 | 2 | 1 | 2 |
| Columbia-Jefferson City | Missouri | Howard | 4 | 677 | 2 | 2 | 2 |
| Missouri non-MSA | Missouri | Madison | 13 | 1296 | 1 | 4 | 6 |
| Missouri non-MSA | Missouri | Chariton | 3 | 385 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Daviess | 10 | 532 | 1 | 3 | 3 |
| Missouri non-MSA | Missouri | Mississippi | 20 | 1181 | 1 | 2 | 2 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1015 | 1 | 3 | 2 |
| Kansas City | Missouri | Caldwell | 8 | 599 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | St. Clair | 6 | 514 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Ralls | 9 | 721 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Shannon | 9 | 450 | 1 | 2 | 1 |
| Missouri non-MSA | Missouri | Montgomery | 10 | 547 | 1 | 1 | 3 |
| Missouri non-MSA | Missouri | Shelby | 5 | 331 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Schuyler | 1 | 243 | 1 | 2 | 2 |
| Missouri non-MSA | Missouri | Iron | 1 | 452 | 1 | 2 | 3 |
| Missouri non-MSA | Missouri | Dade | 10 | 396 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Putnam | 2 | 212 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 10 | 454 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 253 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Carter | 7 | 405 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Monroe | 7 | 563 | 0 | 1 | 2 |
| Missouri non-MSA | Missouri | Knox | 2 | 164 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 10 | 346 | 0 | 1 | 0 |
| Missouri non-MSA | Missouri | Worth | 1 | 132 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 155 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Scotland | 3 | 235 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 286 | 0 | 1 | 1 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
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
