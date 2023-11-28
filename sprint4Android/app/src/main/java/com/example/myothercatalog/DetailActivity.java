package com.example.myothercatalog;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.widget.ImageView;
import android.widget.TextView;

import com.bumptech.glide.Glide;

import org.w3c.dom.Text;

public class DetailActivity extends AppCompatActivity {
    public static final String name = "name";
    public static final String description = "description";
    public static final String url = "image_url";
    private String Image_Url;
    private String Description;
    private String Title;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);
        ImageView image_detail_activity = findViewById(R.id.imageview_detail_activity);
        TextView title_detail_activity = findViewById(R.id.text_view_detail_activity);
        TextView description_detail_activity = findViewById(R.id.description_detail_activity);
        Intent intent = getIntent();
        Title = intent.getStringExtra(name);
        Description = intent.getStringExtra(description);
        Image_Url = intent.getStringExtra(url);
        Glide.with(DetailActivity.this).load(Image_Url).into(image_detail_activity);
        title_detail_activity.setText(Title);
        description_detail_activity.setText(Description);
    }
}
