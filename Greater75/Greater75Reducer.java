package Greater75;

import java.io.IOException;
import java.util.*;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;

public class Greater75Reducer extends MapReduceBase implements Reducer <Text, DoubleWritable, Text, DoubleWritable> {
	
    public void reduce(Text key, Iterator<DoubleWritable> values, OutputCollector < Text, DoubleWritable> output, Reporter reporter) throws IOException{
        DoubleWritable value = (DoubleWritable) values.next();
        if(value.get() >= 75.0) {
            output.collect(key,value);
        }
    }
}
