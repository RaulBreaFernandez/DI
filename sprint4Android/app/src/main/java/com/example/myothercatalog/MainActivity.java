package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;
import android.os.Bundle;
import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.JsonArrayRequest;
import com.android.volley.toolbox.Volley;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.util.ArrayList;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private RecyclerView recyclerView;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        recyclerView = (RecyclerView) findViewById(R.id.recycler_view);
        request();
    }
    private void request(){

        List<BookData> book_list = new ArrayList<>();

        JsonArrayRequest request = new JsonArrayRequest
                (Request.Method.GET,
                        "https://raw.githubusercontent.com/RaulBreaFernandez/DI/main/catalog.json",
                        null,
                        new Response.Listener<JSONArray>(){
                            @Override
                            public void onResponse(JSONArray response) {
                                try {
                                    for(int i = 0; i < response.length(); i++){
                                        JSONObject jsonObject = response.getJSONObject(i);
                                        BookData books = new BookData(jsonObject);
                                        book_list.add(books);
                                    }
                                } catch (JSONException e) {
                                    e.printStackTrace();
                                }
                                Adapter adapter = new Adapter(book_list, MainActivity.this);
                                recyclerView.setAdapter(adapter);
                                recyclerView.setLayoutManager(new LinearLayoutManager(MainActivity.this));
                            }
                        },

                        new Response.ErrorListener() {

                            @Override
                            public void onErrorResponse(VolleyError error) {

                                error.printStackTrace();

                            }
                        }
                );

        Volley.newRequestQueue(this).add(request);
    }
}
