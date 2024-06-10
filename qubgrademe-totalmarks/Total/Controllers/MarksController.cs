using Microsoft.AspNetCore.Mvc;

namespace Total.Controllers
{    
    [Route("/")]
    [ApiController]
    public class MarksController : ControllerBase
    {
        [HttpGet]
        public JsonResult Get(string mark_1, string mark_2, string mark_3, string mark_4, string mark_5)
        {
            
            string[] marks = new string[] { mark_1, mark_2, mark_3, mark_4, mark_5 };
            int[] rmarks = new int[5];
            for (int i = 0; i < marks.Length; i++)
            {
                try
                {
                    int formattedMark = Int32.Parse(marks[i]);
                    rmarks[i]=formattedMark;
                }
                catch (FormatException)
                {
                    string errormessage = "Invalid mark provided (must be int) - Mark "+(i+1);
                    return new JsonResult(new
                    {
                        error = true,
                        errormessage = errormessage,
                        output = ""
                    });
                }
            }
            foreach (var mark in rmarks)
            {
                if (0 > mark || mark > 100)
                {
                    return new JsonResult(new
                    {
                        error = true,
                        errormessage = "All marks must be valid integars between 0-100",
                        output = ""
                    });
                }
            }
            

            //Calculate and return total
            var total = 0;
            foreach (int mark in rmarks)
                total += mark;
            var output = new
            {
                error = false,
                errormessage = "",
                output = total
            };
            return new JsonResult(output);
        }
    }
}
