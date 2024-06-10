namespace TestTotal
{
    public class UnitTest1
    {
        [Fact]
        public void TestTotalMarks()
        {
            int [] rmarks = new int[]{100,100,100,100,100};
            var total = 0;
            foreach (int mark in rmarks)
                total += mark;
            
            Assert.Equal(total, 500);
        }
    }
}