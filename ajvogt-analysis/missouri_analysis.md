# COVID-19 Missouri Statistics & Regional Breakdowns
Author: Adam J. Vogt  
Updated: 04/19/2021  
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
| St. Louis-Farmington | 4998 | 287863 | 217 | 325 | 362 |
| St. Joseph | 215 | 13088 | -28 | -11 | -2 |
| Columbia-Jefferson City | 337 | 37879 | -30 | -4 | 9 |
| Joplin | 307 | 20485 | -31 | -9 | 1 |
| Cape Girardeau-Sikeston | 240 | 14951 | -43 | -18 | -4 |
| Springfield | 660 | 43951 | -53 | -12 | 11 |
| Kansas City | 2629 | 198679 | -192 | 0 | 87 |
| Missouri non-MSA | 2163 | 132867 | -335 | -121 | 19 |
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
| St. Louis-Farmington | Missouri | St. Louis | 2145 | 95629 | 162 | 163 | 151 |
| Kansas City | Kansas | Johnson | 739 | 57068 | 53 | 54 | 50 |
| St. Louis-Farmington | Missouri | St. Louis City | 460 | 23408 | 50 | 49 | 42 |
| St. Louis-Farmington | Illinois | Madison | 514 | 29848 | 38 | 34 | 37 |
| St. Louis-Farmington | Illinois | St. Clair | 502 | 27154 | 29 | 30 | 29 |
| Kansas City | Kansas | Wyandotte | 276 | 19966 | 19 | 18 | 15 |
| St. Louis-Farmington | Illinois | Macoupin | 81 | 4593 | 6 | 6 | 4 |
| Kansas City | Kansas | Leavenworth | 90 | 7136 | 5 | 4 | 5 |
| St. Louis-Farmington | Illinois | Monroe | 90 | 4312 | 4 | 6 | 5 |
| St. Louis-Farmington | Illinois | Jersey | 49 | 2624 | 3 | 3 | 3 |
| Kansas City | Kansas | Miami | 41 | 2712 | 3 | 3 | 1 |
| St. Louis-Farmington | Illinois | Bond | 24 | 1976 | 3 | 2 | 1 |
| St. Louis-Farmington | Illinois | Clinton | 90 | 5702 | 1 | 1 | 2 |
| Missouri non-MSA | Missouri | Nodaway | 25 | 2680 | 1 | 1 | 1 |
| Missouri non-MSA | Missouri | Pemiscot | 30 | 1559 | 1 | 1 | 0 |
| Kansas City | Kansas | Linn | 8 | 795 | 0 | 0 | 0 |
| St. Louis-Farmington | Illinois | Calhoun | 2 | 509 | 0 | 0 | 0 |
| St. Joseph | Kansas | Doniphan | 23 | 965 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Atchison | 6 | 445 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Holt | 12 | 432 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Putnam | 4 | 297 | 0 | 0 | 0 |
| Cape Girardeau-Sikeston | Illinois | Alexander | 11 | 462 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Unassigned | 0 | 0 | 0 | 0 | 0 |
| Unassigned/Out of MO | Missouri | Out of MO | 0 | 0 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Schuyler | 6 | 332 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Stone | 41 | 2386 | 0 | 0 | 1 |
| Missouri non-MSA | Missouri | Dent | 17 | 942 | 0 | 1 | 1 |
| Missouri non-MSA | Missouri | Worth | 2 | 162 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Dade | 16 | 573 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Scotland | 3 | 305 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Maries | 8 | 628 | 0 | 0 | 0 |
| Missouri non-MSA | Missouri | Mercer | 2 | 298 | -1 | 0 | 0 |
| St. Louis-Farmington | Missouri | Jefferson | 238 | 22620 | -1 | 23 | 31 |
| Missouri non-MSA | Missouri | Barton | 14 | 1160 | -1 | 0 | 0 |
| Missouri non-MSA | Missouri | Hickory | 15 | 639 | -1 | 0 | 0 |
| Missouri non-MSA | Missouri | Camden | 86 | 4036 | -1 | 1 | 1 |
| Missouri non-MSA | Missouri | Morgan | 43 | 1699 | -1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Moniteau | 31 | 1769 | -1 | 0 | 0 |
| Missouri non-MSA | Missouri | Clark | 7 | 663 | -1 | 0 | 0 |
| Missouri non-MSA | Missouri | Reynolds | 3 | 375 | -1 | 0 | 0 |
| Missouri non-MSA | Missouri | Perry | 30 | 2165 | -1 | 0 | 0 |
| Missouri non-MSA | Missouri | Douglas | 27 | 890 | -1 | 0 | 0 |
| Missouri non-MSA | Missouri | Phelps | 128 | 3764 | -1 | 1 | 4 |
| Missouri non-MSA | Missouri | Miller | 54 | 2513 | -1 | 0 | 0 |
| Missouri non-MSA | Missouri | Wright | 29 | 1547 | -1 | 0 | 0 |
| Missouri non-MSA | Missouri | Chariton | 7 | 661 | -1 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Callaway | 47 | 4903 | -1 | 0 | 1 |
| Missouri non-MSA | Missouri | Mississippi | 28 | 1435 | -1 | 0 | 1 |
| Missouri non-MSA | Missouri | Wayne | 11 | 1028 | -1 | 0 | 0 |
| Missouri non-MSA | Missouri | Knox | 2 | 372 | -1 | 0 | 0 |
| Missouri non-MSA | Missouri | Carter | 9 | 538 | -2 | 0 | 0 |
| Missouri non-MSA | Missouri | Ralls | 12 | 1045 | -2 | 0 | 1 |
| Missouri non-MSA | Missouri | Shannon | 12 | 581 | -2 | 0 | 0 |
| Springfield | Missouri | Webster | 53 | 3529 | -2 | 0 | 1 |
| Missouri non-MSA | Missouri | Gentry | 20 | 822 | -2 | -1 | 0 |
| St. Louis-Farmington | Missouri | Warren | 21 | 3058 | -2 | 0 | 2 |
| Missouri non-MSA | Missouri | Crawford | 36 | 2530 | -2 | 0 | 4 |
| Missouri non-MSA | Missouri | Texas | 23 | 1812 | -2 | 0 | 0 |
| Missouri non-MSA | Missouri | St. Clair | 8 | 775 | -2 | -1 | 0 |
| Missouri non-MSA | Missouri | Ripley | 15 | 1056 | -2 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Cooper | 27 | 1894 | -2 | -1 | 0 |
| Missouri non-MSA | Missouri | Montgomery | 11 | 1020 | -2 | 0 | 0 |
| Missouri non-MSA | Missouri | Laclede | 68 | 3245 | -3 | 0 | 0 |
| Columbia-Jefferson City | Missouri | Howard | 7 | 1042 | -3 | -1 | 0 |
| Missouri non-MSA | Missouri | Sullivan | 14 | 840 | -3 | -1 | 0 |
| Missouri non-MSA | Missouri | Shelby | 7 | 568 | -3 | -1 | 1 |
| Springfield | Missouri | Dallas | 26 | 1234 | -3 | -1 | 0 |
| Missouri non-MSA | Missouri | Monroe | 11 | 996 | -3 | -1 | 0 |
| Missouri non-MSA | Missouri | Ste. Genevieve | 16 | 1793 | -3 | -1 | 0 |
| Columbia-Jefferson City | Missouri | Osage | 14 | 1608 | -3 | -1 | 0 |
| Kansas City | Missouri | Caldwell | 11 | 749 | -3 | -1 | 0 |
| Missouri non-MSA | Missouri | New Madrid | 43 | 2091 | -3 | -1 | 0 |
| Missouri non-MSA | Missouri | Grundy | 34 | 982 | -3 | -1 | 0 |
| Missouri non-MSA | Missouri | Madison | 16 | 1608 | -3 | 0 | 0 |
| Cape Girardeau-Sikeston | Missouri | Bollinger | 12 | 1101 | -4 | -1 | 0 |
| Missouri non-MSA | Missouri | Pettis | 78 | 5062 | -4 | 0 | 0 |
| Missouri non-MSA | Missouri | Benton | 30 | 1644 | -4 | -1 | 0 |
| Missouri non-MSA | Missouri | Dunklin | 21 | 2768 | -4 | 0 | 1 |
| Missouri non-MSA | Missouri | Taney | 92 | 5189 | -4 | 0 | 0 |
| Kansas City | Missouri | Bates | 27 | 1299 | -4 | -1 | 0 |
| St. Joseph | Missouri | DeKalb | 31 | 1122 | -4 | -2 | 0 |
| Missouri non-MSA | Missouri | Pulaski | 51 | 3427 | -4 | -1 | 0 |
| Missouri non-MSA | Missouri | Cedar | 21 | 1061 | -4 | -2 | 0 |
| Missouri non-MSA | Missouri | Henry | 38 | 1984 | -4 | -2 | 0 |
| Missouri non-MSA | Missouri | Barry | 45 | 2866 | -4 | -1 | 0 |
| Missouri non-MSA | Missouri | Pike | 23 | 1764 | -5 | -2 | 0 |
| Missouri non-MSA | Missouri | Iron | 6 | 865 | -5 | -2 | -1 |
| Missouri non-MSA | Missouri | Ozark | 17 | 642 | -5 | -2 | 0 |
| Missouri non-MSA | Missouri | Stoddard | 37 | 2460 | -5 | -2 | 0 |
| St. Joseph | Missouri | Andrew | 19 | 1842 | -5 | -2 | 0 |
| Kansas City | Missouri | Ray | 27 | 1921 | -5 | -1 | 0 |
| Missouri non-MSA | Missouri | Butler | 41 | 4139 | -5 | -1 | 1 |
| Missouri non-MSA | Missouri | Daviess | 11 | 697 | -5 | -2 | -1 |
| Missouri non-MSA | Missouri | Carroll | 23 | 1025 | -6 | -2 | 0 |
| Missouri non-MSA | Missouri | Linn | 12 | 1168 | -6 | -3 | 0 |
| Missouri non-MSA | Missouri | McDonald | 26 | 2314 | -7 | -2 | 0 |
| Kansas City | Missouri | Platte | 46 | 4059 | -7 | -1 | 1 |
| St. Louis-Farmington | Missouri | Lincoln | 40 | 5628 | -7 | 2 | 6 |
| Cape Girardeau-Sikeston | Missouri | Scott | 83 | 4666 | -7 | -3 | 0 |
| Missouri non-MSA | Missouri | Harrison | 14 | 874 | -7 | -3 | -1 |
| Columbia-Jefferson City | Missouri | Boone | 89 | 17651 | -7 | 3 | 7 |
| Missouri non-MSA | Missouri | Lewis | 12 | 992 | -7 | -3 | 5 |
| Missouri non-MSA | Missouri | Oregon | 3 | 794 | -8 | -3 | -1 |
| Missouri non-MSA | Missouri | Adair | 19 | 2349 | -8 | -4 | 0 |
| Missouri non-MSA | Missouri | Lawrence | 80 | 3363 | -8 | -3 | 0 |
| Missouri non-MSA | Missouri | Washington | 49 | 2682 | -8 | -3 | -1 |
| Missouri non-MSA | Missouri | Macon | 15 | 1530 | -8 | -3 | 0 |
| Missouri non-MSA | Missouri | Gasconade | 44 | 1514 | -8 | -3 | -1 |
| Missouri non-MSA | Missouri | Marion | 44 | 3576 | -9 | -2 | 14 |
| Missouri non-MSA | Missouri | Randolph | 30 | 2619 | -10 | -3 | 0 |
| Columbia-Jefferson City | Missouri | Cole | 122 | 9012 | -10 | -3 | 0 |
| Joplin | Missouri | Newton | 74 | 5210 | -10 | -3 | 0 |
| Springfield | Missouri | Christian | 89 | 8274 | -11 | -2 | 1 |
| Missouri non-MSA | Missouri | Audrain | 57 | 2691 | -11 | -5 | -1 |
| Missouri non-MSA | Missouri | Livingston | 40 | 1650 | -11 | -5 | -2 |
| Missouri non-MSA | Missouri | Vernon | 43 | 1907 | -11 | -4 | 0 |
| Missouri non-MSA | Missouri | Howell | 43 | 3429 | -11 | -5 | 0 |
| Missouri non-MSA | Missouri | Saline | 38 | 2815 | -11 | -5 | -2 |
| Kansas City | Missouri | Lafayette | 56 | 3003 | -12 | -5 | -1 |
| Springfield | Missouri | Polk | 33 | 3192 | -13 | -5 | 0 |
| St. Louis-Farmington | Missouri | Franklin | 179 | 10435 | -13 | -1 | 6 |
| Kansas City | Missouri | Clinton | 65 | 1931 | -16 | -7 | -3 |
| Kansas City | Missouri | Cass | 104 | 8954 | -17 | -2 | 3 |
| St. Joseph | Missouri | Buchanan | 142 | 9159 | -18 | -7 | -1 |
| St. Louis-Farmington | Missouri | St. Francois | 115 | 8687 | -18 | -7 | -1 |
| Joplin | Missouri | Jasper | 233 | 15275 | -21 | -6 | 1 |
| Springfield | Missouri | Greene | 459 | 27722 | -23 | -3 | 8 |
| Kansas City | Missouri | Clay | 163 | 9728 | -24 | -8 | 0 |
| Cape Girardeau-Sikeston | Missouri | Cape Girardeau | 134 | 8722 | -31 | -13 | -4 |
| Missouri non-MSA | Missouri | Johnson | 49 | 4719 | -32 | -15 | -4 |
| St. Louis-Farmington | Missouri | St. Charles | 448 | 41680 | -40 | 9 | 38 |
| Kansas City | Missouri | Kansas City | 564 | 42518 | -73 | -15 | 12 |
| Kansas City | Missouri | Jackson | 412 | 36840 | -110 | -37 | 0 |
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
