# include<iostream>
# include<bits/stdc++.h>


using namespace std;


map<pair<vector<vector<int>>,int>,vector<vector<vector<int>>>> states;


void dfs(int i,int j,int depth,vector<vector<int>> a){
    if(depth > 8){
        return;
    }




    // up movement


    if(i-1 >= 0){
            // cout<<"here"<<endl;
            vector<vector<int>> temp(3,vector<int>(3));
            for(int i = 0;i<3;i++){
                for(int j = 0;j<3;j++){
                    temp[i][j] = a[i][j];
                }
            }
            a[i][j] = a[i-1][j];
            a[i-1][j] = 0;


            // temp is father
            // now a is son . right yeah right .
            // depth + 1 has happened


            vector<vector<vector<int>>> fun;
           


            for(auto it : states[make_pair(temp,depth)]){
                vector<vector<int>> temp1(3,vector<int>(3));
                for(int i = 0;i<3;i++){
                    for(int j = 0;j<3;j++){
                        temp1[i][j] = it[i][j];
                    }
                }
                fun.push_back(temp1);
            }


            pair<vector<vector<int>>,int> var = make_pair(a,depth+1);
            states[var] = fun;
            states[var].push_back(temp);


            dfs(i-1,j,depth+1,a);
            a[i-1][j] = a[i][j];
            a[i][j] = 0;
        }
    // down movement
        if(i+1 < 3){
                        // cout<<"ahere"<<endl;


            vector<vector<int>> temp(3,vector<int>(3));
            for(int i = 0;i<3;i++){
                for(int j = 0;j<3;j++){
                    temp[i][j] = a[i][j];
                }
            }


            a[i][j] = a[i+1][j];
            a[i+1][j] = 0;




            vector<vector<vector<int>>> fun;
           


            for(auto it : states[make_pair(temp,depth)]){
                vector<vector<int>> temp1(3,vector<int>(3));
                for(int i = 0;i<3;i++){
                    for(int j = 0;j<3;j++){
                        temp1[i][j] = it[i][j];
                    }
                }
                fun.push_back(temp1);
            }


            pair<vector<vector<int>>,int> var = make_pair(a,depth+1);
            states[var] = fun;
            states[var].push_back(temp);
            dfs(i+1,j,depth+1,a);
            a[i+1][j] = a[i][j];
            a[i][j] = 0;
        }
    // left movement
        if(j-1 >= 0){
                        // cout<<"bhere"<<endl;


            vector<vector<int>> temp(3,vector<int>(3));
            for(int i = 0;i<3;i++){
                for(int j = 0;j<3;j++){
                    temp[i][j] = a[i][j];
                }
            }


            a[i][j] = a[i][j-1];
            a[i][j-1] = 0;
            vector<vector<vector<int>>> fun;
           


            for(auto it : states[make_pair(temp,depth)]){
                vector<vector<int>> temp1(3,vector<int>(3));
                for(int i = 0;i<3;i++){
                    for(int j = 0;j<3;j++){
                        temp1[i][j] = it[i][j];
                    }
                }
                fun.push_back(temp1);
            }


            pair<vector<vector<int>>,int> var = make_pair(a,depth+1);
            states[var] = fun;
            states[var].push_back(temp);
            dfs(i,j-1,depth+1,a);
            a[i][j-1] = a[i][j];
            a[i][j] = 0;
        }
    // right movement
        if(j+1 < 3){
                        // cout<<"chere"<<endl;


            vector<vector<int>> temp(3,vector<int>(3));
            for(int i = 0;i<3;i++){
                for(int j = 0;j<3;j++){
                    temp[i][j] = a[i][j];
                }
            }


            a[i][j] = a[i][j+1];
            a[i][j+1] = 0;
            vector<vector<vector<int>>> fun;
           


            for(auto it : states[make_pair(temp,depth)]){
                vector<vector<int>> temp1(3,vector<int>(3));
                for(int i = 0;i<3;i++){
                    for(int j = 0;j<3;j++){
                        temp1[i][j] = it[i][j];
                    }
                }
                fun.push_back(temp1);
            }


            pair<vector<vector<int>>,int> var = make_pair(a,depth+1);
            states[var] = fun;
            states[var].push_back(temp);


            dfs(i,j+1,depth+1,a);
        }




}
int main(){
    ios:: sync_with_stdio(false);
    cin.tie(NULL);


    vector<vector<int>> a(3,vector<int>(3));


    for(int i = 0;i<3;i++){
        for(int j = 0;j<3;j++){
            cin>>a[i][j];
        }
    }




    int x,y;
    cin>>x>>y;


    dfs(x,y,1,a);


    vector<vector<int>> input(3,vector<int>(3));
    for(int i = 0;i<3;i++){
        for(int j = 0;j<3;j++){
            cin>>input[i][j];
        }
    }


    int d;
    cin>>d;




    for(auto it : states[make_pair(input,d)]){
        for(int i = 0;i<3;i++){
            for(int j = 0;j<3;j++){
                cout<<it[i][j]<<" ";
            }
            cout<<endl;
        }
        cout<<"the new one is as follows."<<endl;
    }


    // for(auto it : states){
    //  cout<<"depth = "<<it.first.second<<endl;
    //  cout<<it.first.first.size()<<"fuck"<<endl;
    //  for(auto ix : it.first.first){
    //      for(auto im : ix){
    //          cout<<im<<" ";
    //      }
    //      cout<<endl;
    //  }
    //  cout<<"The series is as follows."<<endl;
    //  cout<<it.second.size()<<" = sizer()"<<endl;


    //  for(auto iv : it.second){
    //      for(int i = 0;i<3;i++){
    //          for(int j = 0;j<3;j++){
    //              cout<<iv[i][j]<<" ";
    //          }
    //          cout<<endl;
    //      }
    //      cout<<endl;
    //  }


    //  cout<<"this ends here";


    //  cout<<endl;
    // }


    return 0;
}
