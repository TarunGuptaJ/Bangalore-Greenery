package Greater75;

import java.io.IOException;

import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.DoubleWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapred.*;

public class Greater75Mapper extends MapReduceBase implements Mapper <LongWritable, Text, Text, DoubleWritable> {
	
	public void map(LongWritable key, Text value, OutputCollector <Text, DoubleWritable> output, Reporter reporter) throws IOException {

		String valueString = value.toString();
		String[] data = valueString.split(",");
		Text fileName = new Text(data[0]);
		DoubleWritable percentage = new DoubleWritable(Double.parseDouble(data[1]));
		output.collect(fileName,percentage);
	}
}
