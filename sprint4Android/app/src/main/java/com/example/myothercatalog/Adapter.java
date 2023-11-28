package com.example.myothercatalog;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;
import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;
import com.bumptech.glide.Glide;
import java.util.List;

public class Adapter extends RecyclerView.Adapter<Adapter.MyViewHolder> {

    private final List<BookData> book_Data;
    private final LayoutInflater layoutInflater;
    private final Context context;

    public Adapter(List<BookData> bookData, Context context) {
        this.book_Data = bookData;
        this.context = context;
        this.layoutInflater = LayoutInflater.from(context);
    }

    @NonNull
    @Override
    public Adapter.MyViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = layoutInflater.inflate(R.layout.element, parent,false);
        return new MyViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull Adapter.MyViewHolder holder, int position) {
        BookData bookData = book_Data.get(position);
        holder.title.setText(bookData.getTitle());
        Glide.with(context).load(bookData.getUrl()).into(holder.image);

    }

    @Override
    public int getItemCount() {
        return book_Data.size();
    }

    public static class MyViewHolder extends RecyclerView.ViewHolder{

        ImageView image;
        TextView title;

        public MyViewHolder(@NonNull View itemView) {
            super(itemView);
            image = itemView.findViewById(R.id.iconImageView);
            title = itemView.findViewById(R.id.book_title);

        }

    }

}
