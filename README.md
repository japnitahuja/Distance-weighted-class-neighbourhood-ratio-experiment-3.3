# A Distance-Weighted Class-Homogeneous Neighbourhood Ratio for Algorithm Selection Experiment 3.3

Link to paper: http://proceedings.mlr.press/v129/chen20a/chen20a.pdf

To establish that β-frequencies capture the information that other complexity measures do, the following preliminary experimentation was conducted. We generated binary-classed base-level artificial datasets of different configurations in a 2-D Euclidean plane.

![Screenshot 2022-03-17 133320](https://user-images.githubusercontent.com/10168783/158860851-1947f81b-0d2f-4ed2-b410-2b5e5139c985.jpg)

All the clusters initially had a separation of 290 units from the centroid, and in each iteration the separation was reduced by 10 units, causing the clusters to move towards the centroid and eventually merging together. We generated 20 datasets in each iteration, amounting to a total of 600 datasets for each configuration.

For each dataset, we calculated the R2 value for the linear regression model, where the dependent variable is a complexity measure, and the independent variables corresponded to the 10-bin β-frequencies.

Results and discussion can be found in Section 3.3 of http://proceedings.mlr.press/v129/chen20a/chen20a.pdf
