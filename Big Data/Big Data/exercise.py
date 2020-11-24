import numpy as np
import pandas as pd
import os

#INTECH IT EXERCISE
#Author: Chanon Kachorn


#loading the data
data = pd.read_csv(os.getcwd() + "\Desktop\IT course October 2020\Big Data\MOCK_DATA.csv", delimiter=',')



#BASIC LEVEL QUESTIONS
####################################################################################################
# How many columns are there?
# print (data.columns) #4 'Product', 'Value', 'Location', 'Time'
# print(data.info)


# How many customers are there in total?
# print(len(data)) # 10 thousand
# print(data)


# How many products, location, time are there?
# print(data.Product.unique()) #['Tomato' 'Fish' 'Shampoo' 'Carrot' 'Soap' 'Banana' 'Pie' 'Orange'
                               # 'Cookie' 'Chicken'] == 10 products
# print(data.Location.unique()) #['Canberra' 'Sydney' 'Melbourne' 'Perth' 'Brisbane'] == 5 locations
# print(data.Time.unique())    #['Morning' 'Afternoon']  == 2 times


# What is the total sales values? (sum of sales)
# print(data['Value'].sum()) #524322


# What is the average sales values?
# print(data['Value'].mean()) #52.4322


# Are there more customers in the Morning or Afternoon?
# print(data[data.Time == 'Morning'].count()) #4920
# print(data[data.Time == 'Afternoon'].count()) #5080 So Afternoon more!
# print(data[data.Time == 'Morning'].count() > data[data.Time == 'Afternoon'].count())

#INTERMEDIATE LEVEL QUESTIONS
#######################################################################################################


# Which location has the highest and lowest sales count?
# print(data.groupby('Location').count()) #Brisbane 1964, Canberra 2019, 
                                            # Melbourne 2014, Perth 1978, Sydney 2025
                                            #So Sydney is highest and Brisbane is lowest
# print(data.groupby('Location').count().sort_values('Value'))



# Which location has the highest and lowest sales values?
# print(data.groupby('Location').sum()[['Value']]) #Brisbane 102286, Canberra   106651, Melbourne  106510,
                                                # Perth      104926, Sydney     103949. Canberra is highest!
                                                # Sydney is lowest
# print(data.groupby('Location').sum().sort_values('Value'))

# Which location has the highest and lowest average sales value?
# print(data.groupby('Location').mean()['Value']) # Brisbane   52.080448, Canberra   52.823675, 
                                                    # Melbourne  52.884806 Perth      53.046512
                                                    # Sydney     51.332840. So Perth is highest!, 
                                                    # Sydney is lowest
 
# print(data.groupby('Location').mean().sort_values('Value', ascending=[False]))


# Which product has the highest and lowest sales count?
# print(data.groupby('Product').count()) # Banana     992,  Carrot    1030, Chicken    965, Cookie     993,
                                        # Fish      1016, Orange    1038, Pie       1028, Shampoo    991,
                                        #Soap       942, Tomato    1005. So Orange is the most popular
                                        #Shampoo is the least popular


# Which product has the highest and lowest sales value?
# print(data.groupby('Product').sum()[['Value']]) #Banana   51403, Carrot   53399, Chicken  51449, Cookie   52298
                                    #Fish     55440, Orange   53589, Pie      52018, Shampoo  52918
                                    #Soap     49248, Tomato   52560. So Fish is highest and Soap is lowest

# Which product has the highest and lowest average sales value?
# print(data.groupby('Product').mean()[['Value']]) #Banana   51.817540, Carrot   51.843689, Chicken  53.315026
                                                #Cookie   52.666667, Fish     54.566929, Orange   51.627168
                                                #Pie      50.601167, Shampoo  53.398587, Soap     52.280255
                                                #Tomato   52.298507. So Fish is highest and Pie is lowest

#ADVANCED LEVEL QUESTIONS
######################################################################################################

# For each location which product has the highest and least sales count?
# print(data.groupby(['Location', 'Product']).count())
# print(data.groupby(['Location','Product']).count().sort_values('Value').head(1))
# Brisbane  Banana     209   209    # Canberra  Banana     200   200    # Melbourne Banana     189   189
#           Carrot     223   223    #           Carrot     188   188    #           Carrot     214   214
#           Chicken    175   175    #           Chicken    187   187    #           Chicken    199   199
#           Cookie     196   196    #           Cookie     207   207    #           Cookie     208   208
#           Fish       191   191    #           Fish       215   215    #           Fish       199   199
#           Orange     204   204    #           Orange     214   214    #           Orange     194   194
#           Pie        200   200    #           Pie        193   193    #           Pie        208   208
#           Shampoo    174   174    #           Shampoo    217   217    #           Shampoo    210   210
#           Soap       186   186    #           Soap       182   182    #           Soap       192   192
#           Tomato     206   206    #           Tomato     216   216    #           Tomato     201   201

# Perth     Banana     193   193    # Sydney    Banana     201   201
#           Carrot     211   211    #           Carrot     194   194
#           Chicken    190   190    #           Chicken    214   214
#           Cookie     193   193    #           Cookie     189   189
#           Fish       210   210    #           Fish       201   201
#           Orange     212   212    #           Orange     214   214
#           Pie        195   195    #           Pie        232   232
#           Shampoo    189   189    #           Shampoo    201   201
#           Soap       188   188    #           Soap       194   194
#           Tomato     197   197    #           Tomato     185   185

# For each location which product has the highest and least sales value?
# print(data.groupby(['Location', 'Product']).sum())
print(data.groupby(['Location', 'Product']).max())
# Brisbane  Banana   10472  # Canberra  Banana   10536  # Melbourne Banana    9875
#           Carrot   11441  #           Carrot   10221  #           Carrot   11035
#           Chicken   8958  #           Chicken  10275  #           Chicken  10758
#           Cookie   10559  #           Cookie   11045  #           Cookie   10732
#           Fish     10189  #           Fish     11857  #           Fish     10549
#           Orange   10672  #           Orange   11068  #           Orange   10227
#           Pie      10260  #           Pie       9768  #           Pie      10884
#           Shampoo   9539  #           Shampoo  11563  #           Shampoo  11580
#           Soap      9585  #           Soap      9373  #           Soap      9839
#           Tomato   10611  #           Tomato   10945  #           Tomato   11031

# Perth     Banana    9848  # Sydney    Banana   10672
#           Carrot   10970  #           Carrot    9732
#           Chicken  10192  #           Chicken  11266
#           Cookie   10270  #           Cookie    9692
#           Fish     11683  #           Fish     11162
#           Orange   11430  #           Orange   10192
#           Pie       9652  #           Pie      11454
#           Shampoo  10159  #           Shampoo  10077
#           Soap     10278  #           Soap     10173
#           Tomato   10444  #           Tomato    9529

# For each location which product has the highest and least average sales value?
# print(data.groupby(['Location', 'Product']).mean())
# Brisbane  Banana   50.105263  # Canberra  Banana   52.680000  # Melbourne Banana   52.248677
#           Carrot   51.304933  #           Carrot   54.367021  #           Carrot   51.565421
#           Chicken  51.188571  #           Chicken  54.946524  #           Chicken  54.060302
#           Cookie   53.872449  #           Cookie   53.357488  #           Cookie   51.596154
#           Fish     53.345550  #           Fish     55.148837  #           Fish     53.010050
#           Orange   52.313725  #           Orange   51.719626  #           Orange   52.716495
#           Pie      51.300000  #           Pie      50.611399  #           Pie      52.326923
#           Shampoo  54.821839  #           Shampoo  53.285714  #           Shampoo  55.142857
#           Soap     51.532258  #           Soap     51.500000  #           Soap     51.244792
#           Tomato   51.509709  #           Tomato   50.671296  #           Tomato   54.880597

# Perth     Banana   51.025907  # Sydney    Banana   53.094527
#           Carrot   51.990521  #           Carrot   50.164948
#           Chicken  53.642105  #           Chicken  52.644860
#           Cookie   53.212435  #           Cookie   51.280423
#           Fish     55.633333  #           Fish     55.532338
#           Orange   53.915094  #           Orange   47.626168
#           Pie      49.497436  #           Pie      49.370690
#           Shampoo  53.751323  #           Shampoo  50.134328
#           Soap     54.670213  #           Soap     52.438144
#           Tomato   53.015228  #           Tomato   51.508108

# For each location do people like to visit the store in the Morning or Afternoon?
print(data.groupby(['Location', 'Time']).count())
# Brisbane  Afternoon  52750    # Canberra  Afternoon  54111
#           Morning    49536    #           Morning    52540

# Melbourne Afternoon  53012    # Perth     Afternoon  53070
#           Morning    53498    #           Morning    51856


# Sydney    Afternoon  53735
#           Morning    50214

# For each product do people like to purchase them in the Morning or Afternoon?
print(data.groupby(['Product', 'Time']).count())
# Banana  Afternoon  25135  # Carrot  Afternoon  25887
#         Morning    26268  #         Morning    27512

# Chicken Afternoon  25984  # Cookie  Afternoon  26968
#         Morning    25465  #         Morning    25330

# Fish    Afternoon  27968  # Orange  Afternoon  27803
#         Morning    27472  #         Morning    25786

# Pie     Afternoon  27504  # Shampoo Afternoon  27971
#         Morning    24514  #         Morning    24947

# Soap    Afternoon  25728  # Tomato  Afternoon  25730
#         Morning    23520  #         Morning    26830

# For each product where do people like to purchase them?
# print(data.groupby(['Product', 'Location']).count())
# Banana  Brisbane   10472  # Carrot  Brisbane   11441  # Chicken Brisbane    8958
#         Canberra   10536  #         Canberra   10221  #         Canberra   10275
#         Melbourne   9875  #         Melbourne  11035  #         Melbourne  10758
#         Perth       9848  #         Perth      10970  #         Perth      10192
#         Sydney     10672  #         Sydney      9732  #         Sydney     11266

# Cookie  Brisbane   10559  # Fish    Brisbane   10189  # Orange  Brisbane   10672
#         Canberra   11045  #         Canberra   11857  #         Canberra   11068
#         Melbourne  10732  #         Melbourne  10549  #         Melbourne  10227
#         Perth      10270  #         Perth      11683  #         Perth      11430
#         Sydney      9692  #         Sydney     11162  #         Sydney     10192

# Pie     Brisbane   10260  # Shampoo Brisbane    9539  # Soap    Brisbane    9585
#         Canberra    9768  #         Canberra   11563  #         Canberra    9373
#         Melbourne  10884  #         Melbourne  11580  #         Melbourne   9839
#         Perth       9652  #         Perth      10159  #         Perth      10278
#         Sydney     11454  #         Sydney     10077  #         Sydney     10173

# Tomato  Brisbane   10611
#         Canberra   10945
#         Melbourne  11031
#         Perth      10444
#         Sydney      9529