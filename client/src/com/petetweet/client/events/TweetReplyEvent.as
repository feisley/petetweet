// ActionScript file
package com.petetweet.client.events
{
	import flash.events.Event;

	public class TweetReplyEvent extends Event
	{
		public function TweetReplyEvent(username:String, bubbles:Boolean=true, cancelable:Boolean=false)
		{
			super("TweetReplyEvent", bubbles, cancelable);
			
			this.username = username;
		}
		
		public var username:String;
		
		override public function clone():Event {
			return new TweetReplyEvent(username);
		}
		
	}
}